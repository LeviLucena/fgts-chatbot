from app.services import get_endereco_por_cep
from app.utils import validar_cpf
import re

class ChatbotFGTS:
    def __init__(self):
        self.estado = "apresentacao"
        self.contexto = {}

    def responder(self, entrada):
        if self.estado == "apresentacao":
            self.estado = "coleta_nome"
            return "Olá! Sou assistente virtual do saque FGTS. Vamos começar a simulação. Qual seu nome completo?"

        elif self.estado == "coleta_nome":
            self.contexto['nome'] = entrada.strip()
            self.estado = "coleta_cpf"
            return f"Prazer, {self.contexto['nome']}! Agora, por favor, informe seu CPF:"

        elif self.estado == "coleta_cpf":
            if validar_cpf(entrada):
                self.contexto['cpf'] = entrada
                self.estado = "coleta_cep"
                return "Ótimo! Agora informe seu CEP:"
            else:
                return "CPF inválido. Por favor, digite no formato 000.000.000-00"

        elif self.estado == "coleta_cep":
            cep = re.sub(r'\D', '', entrada)
            endereco = get_endereco_por_cep(cep)
            if endereco:
                self.contexto['endereco'] = endereco
                self.estado = "confirma_endereco"
                return f"Encontrei: {endereco['logradouro']}, {endereco['bairro']}, {endereco['localidade']} - {endereco['uf']}. Está correto? (sim/não)"
            else:
                return "CEP inválido ou API fora do ar. Tente novamente."

        elif self.estado == "confirma_endereco":
            if entrada.lower() in ['sim', 's']:
                self.estado = "coleta_numero"
                return "Qual o número do seu endereço?"
            else:
                self.estado = "coleta_cep"
                return "Ok. Informe o CEP novamente:"

        elif self.estado == "coleta_numero":
            self.contexto['numero'] = entrada.strip()
            self.estado = "coleta_complemento"
            return "Complemento (se houver, senão digite 'nenhum'):"

        elif self.estado == "coleta_complemento":
            self.contexto['complemento'] = entrada
            self.estado = "confirmacao_dados"
            resumo = f"""
Confirmando os dados:
Nome: {self.contexto['nome']}
CPF: {self.contexto['cpf']}
Endereço: {self.contexto['endereco']['logradouro']}, {self.contexto['numero']} {self.contexto['complemento']}, {self.contexto['endereco']['bairro']}, {self.contexto['endereco']['localidade']} - {self.contexto['endereco']['uf']}
"""
            return resumo + "\nEstá tudo correto? (sim/não)"

        elif self.estado == "confirmacao_dados":
            if entrada.lower() in ['sim', 's']:
                self.estado = "despedida"
                return f"Perfeito, {self.contexto['nome']}! Sua simulação foi registrada. Desejamos sucesso com seu saque FGTS. Até logo!"
            else:
                self.estado = "coleta_nome"
                return "Vamos reiniciar. Qual seu nome completo?"

        elif self.estado == "despedida":
            return "Sessão finalizada."

        else:
            return "Desculpe, algo saiu do controle. Reiniciando fluxo..."

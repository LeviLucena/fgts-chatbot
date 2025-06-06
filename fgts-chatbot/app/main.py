from flask import Flask, render_template, request, session, jsonify
import requests
import re
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "chavepadrao")

# CPF regex
def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i+1) - j) for j in range(i))
        resto = (soma * 10) % 11
        if resto == 10: resto = 0
        if resto != int(cpf[i]):
            return False
    return True

# Conversa simulada
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    context = session.get("context", {
        "step": 1,
        "nome": "",
        "cpf": "",
        "cep": "",
        "endereco": {},
        "numero": "",
        "complemento": ""
    })

    step = context["step"]
    resposta = ""

    if "fgts" not in session:
        session["fgts"] = True
        resposta = ("Olá! Sou o assistente virtual especializado em saque FGTS. "
                    "Posso te ajudar com sua simulação. Vamos começar!\n"
                    "Qual o seu nome completo?")
        context["step"] = 2

    elif step == 2:
        context["nome"] = user_input.strip()
        resposta = f"Prazer, {context['nome']}! Agora, por favor, informe seu CPF:"
        context["step"] = 3

    elif step == 3:
        cpf = re.sub(r'\D', '', user_input)
        if not validar_cpf(cpf):
            resposta = "CPF inválido. Por favor, insira um CPF válido no formato 000.000.000-00:"
        else:
            context["cpf"] = cpf
            resposta = "Ótimo! Agora me diga seu CEP para verificarmos seu endereço:"
            context["step"] = 4

    elif step == 4:
        cep = re.sub(r'\D', '', user_input)
        if len(cep) != 8:
            resposta = "CEP inválido. Por favor, insira um CEP válido com 8 dígitos:"
        else:
            try:
                via_cep = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
                if "erro" in via_cep:
                    resposta = "Não encontrei esse CEP. Tente novamente com outro válido:"
                else:
                    context["cep"] = cep
                    context["endereco"] = via_cep
                    resposta = (f"Endereço encontrado: {via_cep['logradouro']}, {via_cep['bairro']}, "
                                f"{via_cep['localidade']}-{via_cep['uf']}. Informe o número da residência:")
                    context["step"] = 5
            except:
                resposta = "Erro ao consultar o CEP. Tente novamente mais tarde."

    elif step == 5:
        context["numero"] = user_input.strip()
        resposta = "Certo! Agora, por favor, informe o complemento (ou digite 'nenhum'):"
        context["step"] = 6

    elif step == 6:
        context["complemento"] = user_input.strip()
        endereco = context["endereco"]
        resposta = (f"Resumo dos seus dados:\n\n"
                    f"Nome: {context['nome']}\n"
                    f"CPF: {context['cpf']}\n"
                    f"Endereço: {endereco['logradouro']}, {context['numero']} - "
                    f"{endereco['bairro']}, {endereco['localidade']}-{endereco['uf']}, "
                    f"Complemento: {context['complemento']}\n\n"
                    f"Obrigado por utilizar nosso assistente de saque FGTS, {context['nome']}! Até mais.")
        context["step"] = 7

    else:
        resposta = ("Entendo sua curiosidade, mas sou especializado apenas em auxiliar com questões sobre saque FGTS. "
                    "Posso ajudá-lo com sua simulação?")

    session["context"] = context
    return jsonify({"response": resposta})

@app.route("/")
def index():
    session.clear()
    return render_template("chat.html")

@app.route("/fluxo")
def fluxo():
    return render_template("fluxo.html")

if __name__ == "__main__":
    app.run(debug=True)

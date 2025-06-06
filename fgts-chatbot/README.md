## ✅ Visão Geral do Projeto
Nome sugerido do projeto: fgts-chatbot
Este projeto é um sistema de agente conversacional de IA para simulação de saque FGTS, com integração à API ViaCEP, validação de CPF, gerenciamento de estado.

### Tecnologias recomendadas:
- Linguagem: Python 3.10+
- Framework para Chatbot: Rasa, Flask + FSM, ou Langchain simples
- Interface: CLI (mais simples e rápido) ou Web com Flask + HTML
- Validação de CPF: validate-docbr
- API externa: ViaCEP (https://viacep.com.br/ws/{cep}/json/)
- Gerenciamento de contexto: dicionário Python ou FSM (máquina de estados)
- Ambiente configurável: dotenv

## 📂 Estrutura de Diretórios Sugerida
```bash
fgts-chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── chatbot.py           # Lógica conversacional
│   ├── utils.py             # Validação de CPF e outros
│   └── services.py          # Integração com ViaCEP
├── templates/
│   └── chat.html            # (se usar web)
├── static/
│   └── style.css            # (se usar web)
├── .env.example
├── requirements.txt
├── README.md
└── flowchart.png            # Fluxograma do diálogo
```

## 🧠 Lógica do Fluxo Conversacional
Use uma máquina de estados finitos (FSM) para controlar o fluxo. Estados sugeridos:

1.apresentacao
2.coleta_nome
3.coleta_cpf
4.valida_cpf
5.coleta_cep
6.valida_cep
7.confirma_endereco
8.coleta_numero
9.coleta_complemento
10.confirmacao_dados
11.despedida

## Requisitos
Flask==3.0.2
requests==2.31.0
validate-docbr==1.10.0
python-dotenv==1.0.1


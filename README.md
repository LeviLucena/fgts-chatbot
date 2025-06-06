<p align="center">

  <!-- Linguagem Backend -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  </a>

  <!-- Framework Web -->
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask" />
  </a>

  <!-- Front-end Básico -->
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">
    <img src="https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5" />
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">
    <img src="https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3" />
  </a>

  <!-- API / IA -->
  <a href="https://platform.openai.com/">
    <img src="https://img.shields.io/badge/-OpenAI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI" />
  </a>

  <!-- JSON para comunicação -->
  <a href="https://www.json.org/json-en.html">
    <img src="https://img.shields.io/badge/-JSON-000000?style=flat-square&logo=json&logoColor=white" alt="JSON" />
  </a>

  <!-- Hospedagem local ou futura -->
  <a href="#">
    <img src="https://img.shields.io/badge/-localhost-808080?style=flat-square&logo=localhost&logoColor=white" alt="Localhost" />
  </a>

  <!-- Licença e status -->
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square" alt="Status: Em desenvolvimento" />
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT License" />

</p>

![Gemini_Generated_Image_4cqxif4cqxif4cqx](https://github.com/user-attachments/assets/7468a5ef-b48c-4e7f-8e2a-53ca46930620)

# ✅ Visão Geral do Projeto

**Nome sugerido:** `fgts-chatbot`

Este projeto consiste em um sistema de agente conversacional de IA para simulação de saque do FGTS, com funcionalidades de integração à API ViaCEP, validação de CPF e gerenciamento de estado para conduzir o usuário de forma interativa.

---

## Tecnologias Recomendadas
- **Linguagem:** Python 3.10 ou superior
- **Framework de Chatbot:** Rasa, Flask com FSM, ou Langchain (simples)
- **Interface:** CLI (mais rápido e simples) ou Web via Flask + HTML
- **Validação de CPF:** `validate-docbr`
- **API Externa:** ViaCEP (https://viacep.com.br/ws/{cep}/json/)
- **Gerenciamento de fluxo:** Dicionário Python ou Máquina de Estados Finita (FSM)
- **Configuração:** Arquivo `.env` usando `dotenv`

---

## 📂 Estrutura de Diretórios Sugerida

```bash  
fgts-chatbot/  
├── app/  
│   ├── __init__.py  
│   ├── main.py  
│   ├── chatbot.py       # Lógica do fluxo conversacional  
│   ├── utils.py         # Validação de CPF e utilitários diversos  
│   └── services.py      # Integração com ViaCEP  
├── templates/  
│   └── chat.html        # Interface web (se utilizada)  
├── static/  
│   └── style.css        # Arquivos estáticos (CSS, JS, etc.)  
├── .env.example         # Modelo de variáveis de ambiente  
├── requirements.txt     # Dependências do projeto  
├── README.md            # Este arquivo  
└── flowchart.png        # Fluxograma do fluxo de diálogos  
```

## 🧠 Lógica do Fluxo Conversacional
Use uma máquina de estados finitos (FSM) para controlar o fluxo. Estados sugeridos:

## Fluxo do Processo

O fluxo conversacional segue as seguintes etapas:

1. **Apresentação** — Introduz o chatbot e explica sua função.
2. **Coleta do nome** — Solicita o nome do usuário.
3. **Coleta do CPF** — Solicita o CPF do usuário.
4. **Validação do CPF** — Verifica se o CPF digitado é válido.
5. **Coleta do CEP** — Solicita o CEP do endereço do usuário.
6. **Validação do CEP** — Verifica se o CEP é válido e busca informações via ViaCEP.
7. **Confirmação do endereço** — Apresenta o endereço obtido e solicita confirmação.
8. **Coleta do número do endereço** — Solicita o número do endereço.
9. **Coleta do complemento** — Solicita informações adicionais, se houver.
10. **Confirmação dos dados** — Revisa todas as informações antes de finalizar.
11. **Despedida** — Finaliza a conversa com uma mensagem de encerramento.

## ⚙️ Requisitos
- 🐍 **Flask==3.0.2**
- 🌐 **requests==2.31.0**
- 📋 **validate-docbr==1.10.0**
- 🛠️ **python-dotenv==1.0.1**

## 🚀 Como começar
## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/LeviLucena/fgts-chatbot.git
cd fgts-chatbot
```

2. Crie e ative um ambiente virtual (recomendado):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure sua API Key (se necessário)<br>
No arquivo .env na raiz do projeto, inclua sua chave da API:
```bash
SECRET_KEY=sua_chave_secreta_aqui
```

5. Rode a aplicação
Para rodar a aplicação localmente:
```bash
python main.py
```

## 🤝 Contribuições
Sinta-se à vontade para contribuir, sugerir melhorias ou relatar problemas para ajudar a desenvolver este projeto.

## 📄 Licença
Este projeto está licenciado sob a licença MIT — veja [LICENSE](https://github.com/github/gitignore/blob/main/LICENSE) para detalhes.

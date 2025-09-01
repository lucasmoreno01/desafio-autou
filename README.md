# E-mail Classifier

Um projeto Flask para classificar e-mails como **importantes** ou **não importantes** e gerar respostas automáticas de forma contextualizada.

---

## Funcionalidades

- Classificação automática de e-mails em **importante** ou **não importante**.
- Geração de respostas automáticas, formais e genéricas.
- Suporte a upload de arquivos `.txt` ou `.pdf`.
- Interface web simples e responsiva.
- Tradução automática opcional usando `deep-translator`.

---

## Tecnologias

- Python 3.11+
- Flask
- Transformers (HuggingFace)
- PyTorch
- PDF parsing: `pdfplumber` e `PyPDF2`
- Frontend: HTML, CSS, JS simples
---

## Instalação, Uso e Observações

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv env_Flask
# Windows
env_Flask\Scripts\activate
# Linux/macOS
source env_Flask/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Execute a aplicação:
```bash
flask --app app run --debug
```
5. Acesse no navegador:
```bash
http://127.0.0.1:5000
```
6. Faça upload de um e-mail ou digite o conteúdo no formulário e pressione "Enviar".

Observações:

Não é necessário subir a pasta do ambiente virtual (env_Flask) para o GitHub.

Para recriar o ambiente, basta usar requirements.txt.

Atualmente, a resposta gerada pode ser em inglês internamente e traduzida para português antes de mostrar na interface.

import re
from transformers import pipeline

generator = pipeline("text-generation", model="google/flan-t5-small")


def preprocess_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[^\w\s]', '', text)
    return text


def classify_email(email_text: str):
    email_text = preprocess_text(email_text)

    prompt = f"""
Você é um assistente que responde e-mails profissionalmente.
Leia o e-mail abaixo e gere uma resposta curta e educada, mencionando o que foi solicitado.
E-mail: {email_text}
Responda apenas com a categoria ('Produtivo' ou 'Improdutivo') e a resposta.
"""

    result = generator(prompt, max_length=150)

    print(result)
    output_text = result[0]["generated_text"]

    category = "Produtivo" if "Produtivo" in output_text else "Improdutivo"
    response = (
        output_text.replace("Produtivo", "").replace("Improdutivo", "").strip()
    )

    return {"category": category, "response": response}

import re
from transformers import pipeline
from PyPDF2 import PdfReader
from deep_translator import GoogleTranslator

model_name = "google/flan-t5-base"

responder = pipeline("text2text-generation", model=model_name, device=-1)


def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def classify_text_email(text):
    text = preprocess_text(text)

    keywords = ["preciso", "quando", "solicito",
                "atualização", "dúvida", "urgente", "reunião", "ajuda"]
    category = "Produtivo" if any(word in text.lower()
                                  for word in keywords) else "Improdutivo"

    text_en = GoogleTranslator(source='pt', target='en').translate(text)

    prompt = f"""
You are a professional email assistant.

I received the following email. Generate a short, polite, and formal response that:
- Stays within the context of the email.
- Can be generic like "I will check and reply soon" or "I will respond when possible".
- Does not repeat the email.
- Does not add external information.

Email: {text_en}
Response:
"""

    response_en = responder(prompt, max_new_tokens=150)[0]["generated_text"]

    response_pt = GoogleTranslator(
        source='en', target='pt').translate(response_en)

    return {"category": category, "response": response_pt}


def classify_file_email(filepath):
    content = ""
    if filepath.lower().endswith(".pdf"):
        reader = PdfReader(filepath)
        for page in reader.pages:
            content += page.extract_text() + "\n"
    else:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    return classify_text_email(content)

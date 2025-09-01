from flask import Blueprint, request, render_template
from models.email_model import classify_text_email, classify_file_email
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

email_blueprint = Blueprint("email", __name__)


@email_blueprint.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@email_blueprint.route("/classify", methods=["POST"])
def classify():
    text_content = ""
    file = request.files.get("email")
    
    if file and file.filename != "":
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        result = classify_file_email(filepath)
    else:
        text_content = request.form.get("email", "")
        result = classify_text_email(text_content)

    return render_template("index.html", result=result)


import os
from flask import Flask
from controllers.email_controller import email_blueprint

app = Flask(__name__)
app.register_blueprint(email_blueprint)

if __name__ == "__main__":
    app.run()

import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config["UPLOAD_FOLDER"] = "uploads/"
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

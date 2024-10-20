import os
from fastapi import FastAPI
from dotenv import load_dotenv
from .routes import router

load_dotenv()

app = FastAPI()


app.config = {"UPLOAD_FOLDER": "uploads/"}
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True) # Create uploads folder if it doesn't exist

app.include_router(router)
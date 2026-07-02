import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "papermind_secret_key")

    # Read the API key from the .env file
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    UPLOAD_FOLDER = "uploads"

    CHROMA_DB = "chroma_db"

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///papermind.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
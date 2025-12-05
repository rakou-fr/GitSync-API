import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    REPO = os.getenv("REPO")
    FILE_PATH = os.getenv("FILE_PATH")

settings = Settings()

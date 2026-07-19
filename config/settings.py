import os
from dotenv import load_dotenv

#load environment variables from .env
load_dotenv()

#API CONFIG
ADZUNA_BASE_URL = "https://api.adzuna.com/v1/api"

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_API_KEY = os.getenv("ADZUNA_API_KEY")

#DATABASE CONFIG
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD") 
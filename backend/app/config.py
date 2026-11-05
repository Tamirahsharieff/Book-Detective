import os
from pathlib import Path
from dotenv import load_dotenv

# Locate the project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Load the .env file
ENV_FILE = BASE_DIR / ".env"
load_dotenv(ENV_FILE, override=True)

# Read database settings
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Create database URL
DATABASE_URL = (
    f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
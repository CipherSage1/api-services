import os
from dotenv import load_dotenv
from pathlib import Path

# Automatically load .env from the root directory
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Read env vars
BASE_URL = os.getenv("BASE_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRATION_MINUTES = int(os.getenv("JWT_EXPIRATION_MINUTES", 60))
PASSWORD_HASH_KEY = os.getenv("PASSWORD_HASH_KEY")
API_KEY = os.getenv("API_KEY")
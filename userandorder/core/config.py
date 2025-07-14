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
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Validate required env vars
if not BASE_URL:
    raise ValueError("BASE_URL is not set. Please check your .env file.")
if not JWT_SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY is not set. Please check your .env file.")
if not JWT_ALGORITHM:
    raise ValueError("JWT_ALGORITHM is not set. Please check your .env file.")  
if not JWT_EXPIRATION_MINUTES:
    raise ValueError("JWT_EXPIRATION_MINUTES is not set. Please check your .env file.")
if not PASSWORD_HASH_KEY:
    raise ValueError("PASSWORD_HASH_KEY is not set. Please check your .env file.")
if not API_KEY:
    raise ValueError("API_KEY is not set. Please check your .env file.")
if not ENVIRONMENT:
    raise ValueError("ENVIRONMENT is not set. Please check your .env file.")
if ENVIRONMENT not in ["development", "staging", "production"]:
    raise ValueError("ENVIRONMENT must be either 'development', 'staging' or 'production'. Please check your .env file.") 
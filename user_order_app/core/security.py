from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from typing import Any, Dict

from user_order_app.core.config import JWT_ALGORITHM, JWT_EXPIRATION_MINUTES, JWT_SECRET_KEY
 
def generate_jwt_token(user_id: str) -> str:
    expiry = datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    payload: Dict[str, Any] = {
        "sub": user_id,
        "exp": expiry,
        "iat": datetime.now(timezone.utc)
    }
    token = jwt.encode(payload, str(JWT_SECRET_KEY), algorithm=str(JWT_ALGORITHM))
    return token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher():
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str):
        return pwd_context.hash(password)
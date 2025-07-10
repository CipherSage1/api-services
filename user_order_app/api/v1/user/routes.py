from fastapi import APIRouter

from models.user_model import  UserListResponse
from services.user_service import get_all_users

router = APIRouter()

@router.get("/", response_model=UserListResponse)
def getUsers():
    return  get_all_users()
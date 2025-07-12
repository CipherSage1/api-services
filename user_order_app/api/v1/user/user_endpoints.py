from fastapi import APIRouter, Request

from models.user_model import  User, UserPatch
from services.user_service import create_user, delete_user, get_all_users, get_user_by_id, update_user
from user_order_app.core.security import Hasher
from user_order_app.models.base_response_model import BaseAPIResponse

router = APIRouter()

@router.get("/all", response_model=BaseAPIResponse)
def getUsers(request: Request):
    print("👥 Fetching all users...", request.state.user)
    return  get_all_users()

@router.get("/{userId}")
def getUserById(userId: str):
    return get_user_by_id(
        userId=userId
    )

@router.get("/", response_model=BaseAPIResponse)
def getCurrentUser(request: Request):
    print("🧪 userId: ", request.state.user)
    return get_user_by_id(
        userId=request.state.user
    )

@router.post("/", response_model=BaseAPIResponse)
def createUser(user: User):
    # hash password before storing
    user.password = Hasher.get_password_hash(user.password)
    return create_user(
        user=user
)

@router.patch("/{userId}", response_model=BaseAPIResponse)
def updateUser(userId:str, user: UserPatch):
    return update_user(
        userId=userId,
        user=user
)

@router.delete("/{userId}", response_model=BaseAPIResponse)
def deleteUser(userId: str):
    return delete_user(
        userId=userId
    )
from fastapi import APIRouter, Request

from models.user_model import  User, UserPatch
from services.user_service import create_user, delete_user, get_all_users, get_user_by_id, update_user
from userandorder.core.security import Hasher
from userandorder.models.base_response_model import BaseAPIResponse

router = APIRouter()

@router.get("/all", response_model=BaseAPIResponse)
def getUsers():
    return  get_all_users()

@router.get("/{userId}")
def getUserById(userId: str):
    return get_user_by_id(
        userId=userId
    )

@router.get("/current", response_model=BaseAPIResponse)
def getCurrentUser(request: Request):
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

@router.patch("/", response_model=BaseAPIResponse)
def updateUser(user: UserPatch, request: Request):
    return update_user(
        userId=request.state.user,
        user=user
)

@router.delete("/", response_model=BaseAPIResponse)
def deleteUser(request: Request):
    return delete_user(
        userId=request.state.user
    )
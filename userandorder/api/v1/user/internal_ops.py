from fastapi import APIRouter
from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.models.user_model import UserPatch
from userandorder.services.user_service import update_user


router = APIRouter()

@router.patch("/user-update/{userId}", response_model=BaseAPIResponse)
def updateUser(userId: str, user: UserPatch):
    return update_user(
        userId=userId,
        user=user
)
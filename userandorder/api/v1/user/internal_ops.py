from fastapi import APIRouter
from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.models.user_model import UserPatch
from userandorder.services.user_service import update_user


router = APIRouter()

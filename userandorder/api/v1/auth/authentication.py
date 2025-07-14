from fastapi import APIRouter

from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.models.request.request_models import LoginRequest
from userandorder.services.auth.auth import log_in_user

router = APIRouter()

@router.post("/login", response_model=BaseAPIResponse)
def loginUser(request: LoginRequest):
    return log_in_user(
        request=request
    )

@router.post("/admin/login", response_model=BaseAPIResponse)
def admiloginUser(request: LoginRequest):
    return log_in_user(
        request=request
    )
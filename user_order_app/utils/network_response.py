
from typing import Any
from fastapi import HTTPException
from user_order_app.models.base_response_model import BaseAPIResponse
def success_response(message: str, data: Any = None, status_code: int = 200) -> BaseAPIResponse:
    return BaseAPIResponse(
        status=status_code,
        message=message,
        error=False,
        data=data
    )


def error_response(message: str, error: bool, status_code: int = 400):
    raise HTTPException(
        status_code=status_code,
        detail={
            "status": status_code,
            "message": message,
            "error": error,
            "data": None
        }
    )
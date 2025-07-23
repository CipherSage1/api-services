
from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.utils.network_response import error_response
from userandorder.utils.http_status_messages import HTTP_STATUS_MESSAGES

from typing import Optional

def get_error_response(status_code: int = 500, _message: Optional[str] = None) -> BaseAPIResponse:
    message = HTTP_STATUS_MESSAGES.get(status_code, "An unknown error occurred.")
    return error_response(message=_message if _message else message, error=True, status_code=status_code)

from userandorder.core.config import ENVIRONMENT
from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.utils.network_response import error_response
from userandorder.utils.http_status_messages import HTTP_STATUS_MESSAGES

def get_error_response(status_code: int, _message: str = "") -> BaseAPIResponse:
    message = HTTP_STATUS_MESSAGES.get(status_code, "An unknown error occurred.")
    if _message and ENVIRONMENT == "development":
        message = message + " " + _message
    return error_response(message=message, error=True, status_code=status_code)

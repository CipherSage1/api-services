from user_order_app.utils.network_response import error_response
from user_order_app.utils.http_status_messages import HTTP_STATUS_MESSAGES

def get_error_response(status_code: int):
    message = HTTP_STATUS_MESSAGES.get(status_code, "An unknown error occurred.")
    return error_response(message=message, error=True, status_code=status_code)

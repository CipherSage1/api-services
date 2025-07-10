import requests

from user_order_app.models.base_response_model import BaseAPIResponse
from user_order_app.utils.network_response import error_response, success_response
from starlette.status import HTTP_200_OK 
 
# URL of your json-server endpoint
baseUrl = "http://localhost:3000"

def get_all_users() -> BaseAPIResponse:
 try:
    response = requests.get(baseUrl+"/users")
    response.raise_for_status()  # Raise error if request failed

    data = response.json() 
    print("👻 Users: ", data)
    return success_response(
      message="",
      data={"users": data},
      status_code=HTTP_200_OK
    )
 
 except requests.exceptions.RequestException as e:
    print("Error fetching data:", str(e))
    return error_response("Failed to fetch users", True, status_code=502)
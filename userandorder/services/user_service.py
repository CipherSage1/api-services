import requests

from userandorder.core.config import BASE_URL
from userandorder.error.error_handler import get_error_response
from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.models.user_model import Role, User, UserPatch
from userandorder.utils.network_response import success_response
from starlette.status import HTTP_200_OK 

baseUrl = str(BASE_URL)

def get_all_users() -> BaseAPIResponse:
 try:
    response = requests.get(baseUrl+"/users")
    response.raise_for_status()  # Raise error if request failed

    data = response.json() 
    print("👥 Fetching all users...")
    return success_response(
      message="✅ Successfully fetched user",
      data={"users": data},
      status_code=HTTP_200_OK
    )

 except requests.exceptions.RequestException as e:
    print("Error fetching data:", str(e))
    return get_error_response(502)

def create_user(user: User) -> BaseAPIResponse:
 try:
    user.role = Role.DEALER
    response = requests.post(baseUrl+"/users", json=user.model_dump(mode="json"))
    if(response.status_code > 299):
      return get_error_response(response.status_code)

    response.raise_for_status
    data = response.json()

    print("✅ Successfully created user: ", data)
    return success_response(
      message="✅ Successfully created user!",
      data={"user":  data}
    )
 except requests.exceptions.RequestException as e:
    print("❌ Error creating user: ", str(e))
    return get_error_response(502)

def get_user_by_id(userId: str) -> BaseAPIResponse:
  try:
    response = requests.get(baseUrl+"/users/"+userId)
    if(response.status_code > 299):
      return get_error_response(response.status_code)
    
    response.raise_for_status

    data = response.json()
    print("✅ User fetched successfully: ", data)
    return success_response(
      message="✅ User fetched successfully!",
      data=data
    )
  except requests.exceptions.RequestException as e:
    print("❌ Error fetching user: ", str(e))
    return get_error_response(502)

def update_user(userId: str, user: UserPatch) -> BaseAPIResponse:
  try:
    update_data = user.model_dump(exclude_unset=True)
    response = requests.patch(baseUrl+"/users/"+userId, json=update_data)
    if(response.status_code > 299):
      return get_error_response(response.status_code)

    response.raise_for_status
    data = response.json()
    print("✅ User updated successfully: ",data)
    return success_response(
      message="✅ User updated successfully!",
      data=data
    )
  except requests.exceptions.RequestException as e:
    print("❌ Error updating user: "+str(e))
    return get_error_response(502)

def delete_user(userId: str) -> BaseAPIResponse:
  try:
    response = requests.delete(baseUrl+"/users/"+userId)
    if(response.status_code > 299):
      return get_error_response(response.status_code)

    response.raise_for_status
    data = response.json()
    print("✅ User deleted successfully: ", data)
    return success_response(
      message="✅ User deleted successfully!",
      data=data
    )
  except requests.exceptions.RequestException as e:
    print("❌ Error deleting user: "+str(e))
    return get_error_response(502)
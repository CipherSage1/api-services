import requests

from userandorder.core.security import Hasher, generate_jwt_token
from userandorder.error.error_handler import get_error_response
from userandorder.models.request.request_models import LoginRequest
from userandorder.models.user_model import User
from userandorder.utils.network_response import success_response

baseUrl = "http://localhost:3000"

def log_in_user(request: LoginRequest):
    try:
        response = requests.get(baseUrl + "/users")
        if response.status_code > 299:
            return get_error_response(response.status_code)
        response.raise_for_status

        users = response.json()
        user_dict = next(
            (
                user for user in users
                if (user['phone'] == request.identifier or user['email'] == request.identifier)
                and Hasher.verify_password(request.password, user['password'])
            ),
            None
        )

        if not user_dict:
            return get_error_response(404)
        
        matching_user = User(**user_dict)
        generated_token = generate_jwt_token(str(matching_user.id))

        print("✅ User Token: ", generated_token)
        return success_response(
            message="✅ Successfully logged in!",
            data={
                "user":{
                    "token":generated_token,
                    "userDetails": matching_user.model_dump(exclude={"password"})
                }
            }
        )
    except requests.exceptions.RequestException as e:
        print("❌ Error Logging in: ", str(e))
        return get_error_response(502)
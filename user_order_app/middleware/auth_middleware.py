
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

from jose import JWTError, jwt

from user_order_app.core.config import API_KEY, JWT_ALGORITHM, JWT_SECRET_KEY 



API_KEY_PROTECTED_PATHS = [
    ("/api/v1/users", "DELETE"),
    ("/api/v1/orders", "POST"),
    ("/api/v1/orders", "GET"),
    ("/api/v1/orders", "DELETE"),
    ("/api/v1/users", "PATCH"),
    ("/api/v1/orders", "PATCH"),
    ("/api/v1/users", "GET")
]

TOKEN_PROTECTED_PATHS = [
    ("/api/v1/users", "GET"),
    ("/api/v1/users", "PATCH"),
    ("/api/v1/users", "DELETE"),
    ("/api/v1/orders", "POST"),
    ("/api/v1/orders", "GET"),
    ("/api/v1/orders", "DELETE"),
]

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        path = request.url.path
        method = request.method.upper()

        for protected_path, protected_method in API_KEY_PROTECTED_PATHS:
            if path.startswith(protected_path) and method == protected_method:
                api_key = request.headers.get("Api_Key")
                if not api_key or api_key != API_KEY:
                    return JSONResponse(
                        status_code=HTTP_403_FORBIDDEN,
                        content={
                            "status": HTTP_403_FORBIDDEN,
                            "message": "Unauthorized. Access to resource denied!",
                            "error": True,
                            "data": None
                        }
                    )
        return await call_next(request)
    
class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        path = request.url.path
        method = request.method.upper()

        for protected_path, protected_method in TOKEN_PROTECTED_PATHS:
            if path.startswith(protected_path) and method == protected_method:
                auth_header = request.headers.get("Authorization")
                if auth_header is None or not auth_header.startswith("Bearer "):
                    return JSONResponse(
                        status_code=HTTP_401_UNAUTHORIZED,
                        content={
                            "status": HTTP_401_UNAUTHORIZED,
                            "message": "Unauthorized. Please provide a valid token.",
                            "error": True,
                            "data": None
                        }
                    )
                
                token = auth_header.split(" ")[1]

                try:
                    payload = jwt.decode(token, str(JWT_SECRET_KEY), algorithms=[str(JWT_ALGORITHM)])
                    request.state.user = payload["sub"]
                
                except JWTError as e:
                    print("❌ Error etractiong token: ", str(e))
                    return JSONResponse(
                        status_code=HTTP_401_UNAUTHORIZED,
                        content={
                            "status": HTTP_401_UNAUTHORIZED,
                            "message": "Unauthorized. Invalid or expired token.",
                            "error": True,
                            "data": None
                        }
                    )

        return await call_next(request)
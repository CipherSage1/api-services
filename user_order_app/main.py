from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_400_BAD_REQUEST


from user_order_app.api.v1.user.user_endpoints import router as user_router
from user_order_app.api.v1.order.order_endpoints import router as order_router
from user_order_app.api.v1.auth.authentication import router as authentication_route

from user_order_app.error.error_handler import get_error_response
from user_order_app.middleware.auth_middleware import AuthMiddleware, JWTAuthMiddleware


app: FastAPI = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    if len(exc.errors()) > 0:
        print("Bad request ", jsonable_encoder(exc.errors()))

    return get_error_response(HTTP_400_BAD_REQUEST)

app.add_middleware(AuthMiddleware)
app.add_middleware(JWTAuthMiddleware)
app.include_router(user_router, prefix="/api/v1/users")
app.include_router(order_router, prefix="/api/v1/orders")
app.include_router(authentication_route, prefix="/api/v1/auth")

@app.get("/")
def root():
    return {"message": "Hello From FastAPI"}

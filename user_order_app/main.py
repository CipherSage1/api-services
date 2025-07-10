from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST


from api.v1.user.routes import router as user_router
from api.v1.order.routes import router as order_router


app: FastAPI = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code= HTTP_400_BAD_REQUEST,
        content={
            "status": HTTP_400_BAD_REQUEST,
            "message": "Bad request body",
            "error": True,
            "data": None,
            "details": jsonable_encoder(exc.errors())  # optional: expose original error list // remove this on production
        }
    )

app.include_router(user_router, prefix="/api/v1/users")
app.include_router(order_router, prefix="/api/v1/orders")

@app.get("/")
def root():
    return {"message": "Hello From FastAPI"}

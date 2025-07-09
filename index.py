from fastapi import FastAPI

from user_service.routes import router as user_router
from order_service.routes import router as order_router

app = FastAPI()


app.include_router(user_router, prefix="/api/v1/users")
app.include_router(order_router,    prefix="/api/v1/orders")

@app.get("/")
def root():
    return{
        "message":"Hello From FastApi"
    }
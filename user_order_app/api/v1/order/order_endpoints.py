from fastapi import APIRouter

from models.order_model import Order
from user_order_app.models.base_response_model import BaseAPIResponse
from user_order_app.services.order_service import create_new_order, delete_order, get_all_orders, get_order_by_id, update_order

router = APIRouter()

@router.get("/", response_model=BaseAPIResponse)
def getOrders():
    return get_all_orders()

@router.get("/{userId}", response_model=BaseAPIResponse)
def getOrderById(userId:str):
    return get_order_by_id(
        userId=userId
    )

@router.post("/", response_model=BaseAPIResponse)
def createOrder(request: Order):
    return create_new_order(
        request=request
    )

@router.patch("/{orderId}", response_model=BaseAPIResponse)
def updateOrder(orderId: str, order: Order):
    return update_order(
        orderId=orderId,
        request=order
    )

@router.delete("/{orderId}", response_model=BaseAPIResponse)
def deleteOrder(orderId: str):
    return delete_order(
        orderId=orderId
        )

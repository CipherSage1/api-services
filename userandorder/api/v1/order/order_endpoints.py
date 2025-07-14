from fastapi import APIRouter, Request

from models.order_model import Order, OrderUpdate
from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.services.order_service import create_new_order, delete_order, get_all_orders, get_order_by_id, update_order

router = APIRouter()

@router.get("/all", response_model=BaseAPIResponse)
def getOrders():
    return get_all_orders()

@router.get("/{userId}", response_model=BaseAPIResponse)
def getOrderById(userId:str):
    return get_order_by_id(
        userId=userId
    )

@router.post("/", response_model=BaseAPIResponse)
def createOrder(order: Order, request: Request):
    order.client_id = request.state.user
    return create_new_order(
        request=order
    )

@router.patch("/{orderId}", response_model=BaseAPIResponse)
def updateOrder(orderId: str, order: OrderUpdate,  request: Request):
    order.client_id = request.state.user  
    return update_order(
        orderId=orderId,
        request=order
    )

@router.delete("/{orderId}", response_model=BaseAPIResponse)
def deleteOrder(orderId: str):
    return delete_order(
        orderId=orderId
        )

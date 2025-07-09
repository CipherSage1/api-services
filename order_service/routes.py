from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Define nested model first
class DeliveryLocation(BaseModel):
    longitude: float  # fixed typo from "lonigute"
    latitude: float
    name:str

class Order(BaseModel):
    id: int
    description: str
    weight: float
    dimentions: str
    type: str
    shipment_type: str
    client_id: int
    delivery_location: DeliveryLocation

class OrderResponse(BaseModel):
    orders: List[Order]

@router.get("/", response_model=OrderResponse)
def getOrders():
    return OrderResponse(
        orders=[
            Order(
                id=0,
                description="Some description detail",
                weight=120.0,
                dimentions="N/A",
                type="Document",
                shipment_type="Standard",
                client_id=0,
                delivery_location= DeliveryLocation(
                    latitude=0.0,
                    longitude=0.0,
                    name="Location name"
                )
            )
        ]
    )
from uuid import uuid4, UUID
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class OrderType(str, Enum):
    DOCUMENT = "Document"
    PERISHABLE = "Perishable"
    FRIDGILE = "Fridgile"
    NORMAL = "Normal"

class ShipmentType(str, Enum):
    STANDARD = "Standard"
    EXPRESS = "Express"
    OVERNIGHT = "Overnight"
    SAMEDAY = "Same Day"

class DeliveryLocation(BaseModel):
    longitude: float
    latitude: float
    name:str

class Dimentions(BaseModel):
    length: Optional[float] = 0.0
    width: Optional[float] = 0.0
    height: Optional[float] = 0.0

class Order(BaseModel):
    id: UUID = Field(default_factory=uuid4)  # ✅ Auto-generate UUID
    description: str
    weight: float
    dimentions: Dimentions
    type: OrderType
    shipment_type: ShipmentType
    client_id: int
    delivery_location: DeliveryLocation

class OrderResponse(BaseModel):
    orders: List[Order]
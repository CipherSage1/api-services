from uuid import uuid4, UUID
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class OrderType(str, Enum):
    DOCUMENT = "Document"
    PERISHABLE = "Perishable"
    FRIDGILE = "Fragile"
    NORMAL = "Normal"


class ShipmentType(str, Enum):
    STANDARD = "Standard"
    EXPRESS = "Express"
    OVERNIGHT = "Overnight"
    SAMEDAY = "NextDay"

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
    client_id: Optional[str] = None  # Assuming client_id is a string   
    delivery_location: DeliveryLocation

class OrderUpdate(BaseModel):
    description: Optional[str] = None
    weight: Optional[float] = None
    dimensions: Optional[Dimentions] = None
    type: Optional[OrderType] = None
    shipment_type: Optional[ShipmentType] = None
    client_id: Optional[int] = None
    delivery_location: Optional[DeliveryLocation] = None

class OrderResponse(BaseModel):
    orders: List[Order]
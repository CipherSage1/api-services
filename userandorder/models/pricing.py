from typing import Dict
from decimal import Decimal
from pydantic import BaseModel
from userandorder.models.order_model import OrderType, ShipmentType 


class Pricing(BaseModel):
    fromLocation: str
    toLocation: str
    shipmentTypesPricing: Dict[ShipmentType, Decimal]
    parcelTypesPricing: Dict[OrderType, Decimal]

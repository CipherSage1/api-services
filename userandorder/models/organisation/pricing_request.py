
from pydantic import BaseModel
from userandorder.models.pricing import Pricing  

class PricingRequest(BaseModel):
    userId: str
    pricing: Pricing
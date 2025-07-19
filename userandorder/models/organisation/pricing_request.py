
from pydantic import BaseModel, Field
from userandorder.models.pricing import Pricing  

class PricingRequest(BaseModel):
    userId: str
    pricing: Pricing
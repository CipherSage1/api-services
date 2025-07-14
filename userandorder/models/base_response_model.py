from typing import Any
from pydantic import BaseModel

class BaseAPIResponse(BaseModel):
    status: int
    message: str
    error: bool
    data: Any
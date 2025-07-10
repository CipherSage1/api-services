from pydantic import BaseModel
from typing import List

class Location(BaseModel):
    longitude: float
    latitude: float
    name: str

class User(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    location: Location

class UserListResponse(BaseModel):
    users: List[User]
    
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

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
    

@router.get("/", response_model=UserListResponse)
def getUsers():
    return UserListResponse(
        users=[
            User(
                id=0,
                name="First User",
                phone="000-0000-000-000",
                email="someemailaddress@gmail.com",
                location=Location(
                    longitude=0.0,
                    latitude=0.0,
                    name="Some Location"
                )
            ),
            User(
                id=1,
                name="Another User",
                phone="000-0000-000-000",
                email="someemailaddress@gmail.com",
                location=Location(
                    longitude=0.0,
                    latitude=0.0,
                    name="Some Location"
                )
            ),
            User(
                id=2,
                name="Third User",
                phone="000-0000-000-000",
                email="someemailaddress@gmail.com",
                location=Location(
                    longitude=0.0,
                    latitude=0.0,
                    name="Some Location"
                )
            )
        ]
    )
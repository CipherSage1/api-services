from enum import Enum
from pydantic import BaseModel, Field
from typing import List
from uuid import uuid4, UUID

class Location(BaseModel):
    longitude: float
    latitude: float
    name: str

class Role(str, Enum):
    ADMIN = "System Admin"
    DEALER = "Dealer"
    AGENT = "Agent"
    USER = "User"

class VerificationDocuments(BaseModel):
    url: str
    description: str

class Verification(BaseModel):
    isPhoneVerified: bool
    isEmailVerified: bool
    identityVerified: bool
    documents: List[VerificationDocuments]

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)  # ✅ Auto-generate UUID
    name: str
    phone: str
    email: str
    password: str
    identity:str
    role: Role
    location: Location
    verification: Verification

class UserListResponse(BaseModel):
    users: List[User]
    
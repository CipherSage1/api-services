from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional
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
    
# Assuming Role, Location, Verification are defined elsewhere
class UserPatch(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    identity: Optional[str] = None
    role: Optional[Role] = None
    location: Optional[Location] = None
    verification: Optional[Verification] = None

class UserListResponse(BaseModel):
    users: List[User]
    
from typing import List, Optional
from pydantic import BaseModel


class Branch(BaseModel):
    branchName: str
    latitude: float
    longitude: float


class Organization(BaseModel):
    companyName: str
    branches: List[Branch]
    kra: str
    companyLogo: str | None = None
    clientId: Optional[str] = None
    id: Optional[str] = None

class OrganizationPatch(BaseModel):
    companyName: str | None = None
    branches: List[Branch] | None = None
    kra: str | None = None
    clientId: str | None = None
    companyLogo: str | None = None
    id: str | None = None
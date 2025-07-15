from typing import List, Optional
from pydantic import BaseModel


class Branch(BaseModel):
    branchId: str
    branchName: str
    latitude: float
    longitude: float


class Organization(BaseModel):
    companyName: str
    branches: List[Branch]
    kra: str
    clientId: Optional[str] = None

class OrganizationPatch(BaseModel):
    companyName: str | None = None
    branches: List[Branch] | None = None
    kra: str | None = None
    clientId: str | None = None

    def model_dump(self, mode="json", exclude_unset=False):
        return super().model_dump(mode=mode, exclude_unset=exclude_unset)
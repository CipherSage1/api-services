from pydantic import BaseModel

from userandorder.models.organisation.organization import Branch

class BranchRequest(BaseModel):
    userId: str
    branch: Branch
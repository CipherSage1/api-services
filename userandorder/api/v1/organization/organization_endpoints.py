from fastapi import APIRouter, Request
from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.models.organisation.organization import Organization
from userandorder.services.organization_service import create_organization

router = APIRouter()

@router.post("/", response_model=BaseAPIResponse)
def createOrganization(organization: Organization, request: Request) -> BaseAPIResponse:
    organization.clientId = request.state.user
    print("Creating organization for user", organization.clientId)
    return create_organization(organization)
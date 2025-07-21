
from fastapi import APIRouter, Request
from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.models.organisation.organization import Organization
from userandorder.models.organisation.pricing_request import PricingRequest
from userandorder.models.pricing import Pricing
from userandorder.services.organization_service import create_organization, update_pricing

router = APIRouter()

@router.post("/", response_model=BaseAPIResponse)
def createOrganization(organization: Organization, request: Request) -> BaseAPIResponse:
    organization.clientId = request.state.user
    return create_organization(organization)

@router.patch("/pricing", response_model=BaseAPIResponse)
def updateOrganization(pricing: Pricing, request: Request) -> BaseAPIResponse:
    return update_pricing(priceRequest= PricingRequest(
        userId=request.state.user,
        pricing=pricing
    ))

@router.post("")
def updateOrganizationBranches() -> BaseAPIResponse:
    return
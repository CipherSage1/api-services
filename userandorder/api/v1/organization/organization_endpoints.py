
from fastapi import APIRouter, Request
from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.models.organisation.branch_request import BranchRequest
from userandorder.models.organisation.organization import Branch, Organization
from userandorder.models.organisation.pricing_request import PricingRequest
from userandorder.models.pricing import Pricing
from userandorder.services.organization_service import create_organization, get_all_branches, get_branch_by_id, update_branches, update_pricing

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

@router.patch("/branches")
def updateOrganizationBranches(branch: Branch, request: Request) -> BaseAPIResponse:
    return update_branches(
        branchRequest= BranchRequest(
            userId=request.state.user,
            branch=branch
        )
    )

@router.get("/branches")
def getAllBranches(request: Request) -> BaseAPIResponse:
    return get_all_branches(
        userId=request.state.user
    )

@router.get("/branch/{userId}/{orgId}")
def getBranchById(userId: str, orgId: str) -> BaseAPIResponse:
    return get_branch_by_id(
        userId=userId,
        orgId=orgId
    )
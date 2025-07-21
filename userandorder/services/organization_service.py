import json
import requests
from fastapi.encoders import jsonable_encoder

from userandorder.core.config import ORGANIZATION_URL
from userandorder.error.error_handler import get_error_response
from userandorder.models.organisation.branch_request import BranchRequest
from userandorder.models.organisation.organization import Organization

from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.models.organisation.pricing_request import PricingRequest
from userandorder.models.user_model import UserPatch
from userandorder.services.user_service import update_user
from userandorder.utils.network_response import success_response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

def create_organization(organization: Organization) -> BaseAPIResponse:
    try:
        response = requests.post(f"{ORGANIZATION_URL}/api/internal/organizations", json=organization.model_dump())
        if response.status_code > 299:
            api_error = BaseAPIResponse(**json.loads(response.content.decode()))
            print("❌ Error creating organization: ",api_error.message)
            return get_error_response(api_error.status, api_error.message)
        response.raise_for_status
        api_data = BaseAPIResponse(**response.json())
        org_data = Organization(**api_data.data)
        if org_data.clientId is not None:
            update_user(
                userId=org_data.clientId,
                user=UserPatch(organizationId=org_data.id)
            )
        else:
            print("❌ Error: clientId is None, cannot update user organizationId.")
        
        print("✅ Organization created successfully: ", org_data)
        return success_response(
            message="✅ Organization created successfully!",
            data= org_data,
            status_code=HTTP_201_CREATED
        )
    except requests.exceptions.RequestException as e:
        print("❌ Error creating organization: ", str(e))
        return get_error_response(502)

def update_pricing(priceRequest: PricingRequest) -> BaseAPIResponse:
    try:
        payload = jsonable_encoder(priceRequest, by_alias=True)

        response = requests.post(f"{ORGANIZATION_URL}/api/internal/organizations/pricing", json=payload)
        if response.status_code > 299:
            api_error = BaseAPIResponse(**json.loads(response.content.decode()))
            print("❌ Error updating organization pricing: ", api_error.message)
            return get_error_response(api_error.status, api_error.message)
        response.raise_for_status()
        api_data = BaseAPIResponse(**response.json())
        print("✅ Organization pricing updated successfully: ", api_data.data)
        return success_response(
            message="✅ Organization pricing updated successfully!",
            data=api_data.data,
            status_code=HTTP_200_OK
        )

    except requests.exceptions.RequestException as e:
        print("❌ Error updating organization pricing: ", str(e))
        return get_error_response(502)
    except Exception as e:
        print("❌ Unexpected error updating organization pricing: ", str(e))
        return get_error_response(500, "❌ Unexpected error occurred while updating organization pricing.")
    
def update_branches(branchRequest: BranchRequest) -> BaseAPIResponse:
    try:
        payload = jsonable_encoder(branchRequest, by_alias=True)
        response = requests.post(f"{ORGANIZATION_URL}/api/internal/organizations/branch", json=payload)
        if response.status_code > 299:
            api_error = BaseAPIResponse(**json.loads(response.content.decode()))
            print("❌ Error updating organization pricing: ", api_error.message)
            return get_error_response(response.status_code)
        response.raise_for_status()
        data = BaseAPIResponse(**response.json())
        print("✅ Organization pricing updated successfully: ", data.data)
        return success_response(
            message="✅ Organization branch updated successfully!",
            data=data,
            status_code=HTTP_200_OK
        )
    except requests.exceptions.RequestException as e:
        print("❌ Error updating organization pricing: ", str(e))
        return get_error_response(502)
    except Exception as e:
        print("❌ Unexpected error updating organization pricing: ", str(e))
        return get_error_response(500, "❌ Unexpected error occurred while updating organization branches.")
    

def get_all_branches(userId: str) -> BaseAPIResponse:
    try:
        response = requests.get("/api/internal/organizations/branch-all/"+userId)
        if response.status_code > 299:
            api_error = BaseAPIResponse(**json.loads(response.content.decode()))
            print("❌ Error updating organization pricing: ", api_error.message)
            return get_error_response(response.status_code)
        data = BaseAPIResponse(**response.json())
        print("✅ Organization list: ", data.data)
        return success_response(
            message="✅ Branches successfully retrieved",
            data=data,
            status_code=response.status_code
        )
    except requests.exceptions.RequestException as e:
        print("❌ Error updating organization pricing: ", str(e))
        return get_error_response(502)
    except Exception as e:
        print("❌ Unexpected error updating organization pricing: ", str(e))
        return get_error_response(500, "❌ Unexpected error occurred while updating organization branches.")
    
def get_branch_by_id(userId: str, orgId: str) -> BaseAPIResponse:
    try:
        response = requests.get("/api/internal/organizations/branch/"+userId+"/"+orgId)
        if response.status_code > 299:
            api_error = BaseAPIResponse(**json.loads(response.content.decode()))
            print("❌ Error updating organization pricing: ", api_error.message)
            return get_error_response(502)
        data = BaseAPIResponse(**response.json())
        print("✅ Branch with id: ", data.data)
        return success_response(
            message="✅ Branch retrieved successfully!",
            data=data.data,
            status_code=response.status_code
        )
    except requests.exceptions.RequestException as e:
        print("❌ Error updating organization pricing: ", str(e))
        return get_error_response(502)
    except Exception as e:
        print("❌ Error updating organization pricing: ", str(e))
        return get_error_response(500, "❌ Unexpected error occurred while updating organization branches.")
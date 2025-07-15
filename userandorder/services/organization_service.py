import requests

from userandorder.core.config import ORGANIZATION_URL
from userandorder.error.error_handler import get_error_response
from userandorder.models.organisation.organization import Organization

from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.utils.network_response import success_response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

def create_organization(organization: Organization):
    try:
        response = requests.post(f"{ORGANIZATION_URL}/api/organizations", json=organization.dict())
        if response.status_code > 299:
            return get_error_response(response.status_code)
        response.raise_for_status

        data = response.json()
        print("🏢 Organization created successfully: ", data)
        return success_response(
            message="🏢 Organization created successfully!",
            data= data,
            status_code=HTTP_201_CREATED
        )
    except requests.exceptions.RequestException as e:
        print("❌ Error creating organization: ", str(e))
        return get_error_response(502)
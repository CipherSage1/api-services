import json
import requests

from userandorder.core.config import ORGANIZATION_URL
from userandorder.error.error_handler import get_error_response
from userandorder.models.organisation.organization import Organization

from userandorder.models.base_response_model import BaseAPIResponse
from userandorder.models.user_model import UserPatch
from userandorder.services.user_service import update_user
from userandorder.utils.network_response import success_response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

def create_organization(organization: Organization):
    try:
        response = requests.post(f"{ORGANIZATION_URL}/api/organizations", json=organization.dict())
        if response.status_code > 299:
            api_error = BaseAPIResponse(**json.loads(response.content.decode()))
            print("❌ Error creating organization: ",api_error.message)
            return get_error_response(api_error.status, api_error.message)
        response.raise_for_status
        api_data = BaseAPIResponse(**response.json())
        org_data = Organization(**api_data.data)

        update_user(
            userId=org_data.clientId,
            user=UserPatch(organizationId=org_data.id)
        )

        print("✅ Organization created successfully: ", org_data)
        return success_response(
            message="✅ Organization created successfully!",
            data= org_data,
            status_code=HTTP_201_CREATED
        )

    except requests.exceptions.RequestException as e:
        print("❌ Error creating organization: ", str(e))
        return get_error_response(502)
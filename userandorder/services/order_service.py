from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_502_BAD_GATEWAY
import requests

 
from userandorder.core.config import BASE_URL 
from userandorder.error.error_handler import get_error_response
from userandorder.utils.network_response import success_response
from userandorder.models.order_model import Order, OrderUpdate
from userandorder.models.base_response_model import BaseAPIResponse

baseUrl = str(BASE_URL)
def get_all_orders() -> BaseAPIResponse:
    try:
        response = requests.get(baseUrl+"/orders")
        if response.status_code > 299:
            return get_error_response(response.status_code)
        response.raise_for_status()

        data = response.json()
        print("👨🏾‍🍳 Orders: ", data)
        return success_response(
            message="✅ Orders fetched successful!",
            data={ "orders":   data },
            status_code=HTTP_200_OK
        )
    
    except requests.exceptions.RequestException  as e:
        print("Error fetching data:", str(e))
        return get_error_response(HTTP_502_BAD_GATEWAY)

def get_order_by_id(userId: str) -> BaseAPIResponse:
    try:
        response = requests.get(baseUrl+"/orders/"+userId)
        if(response.status_code > 299):
            return get_error_response(response.status_code)
        response.raise_for_status

        data = response.json()
        print("✅ Order fetched successfully: ", data)
        return success_response(
            message="✅ Order fetched successfully!",
            data=data
        )
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching order: ", str(e))
        return get_error_response(502)
    
def create_new_order(request: Order)  -> BaseAPIResponse:
    try:
        print("👤 User ID from token in request: ", request.client_id)
        response = requests.post(baseUrl+"/orders", json=request.model_dump(mode="json"))
        if response.status_code > 299:
            return get_error_response(response.status_code, response.reason)
        response.raise_for_status()

        data = response.json()
        print("🆕 Record: ", data)
        return success_response(
            message="✅ Record created successfully!",
            data=data,
            status_code=HTTP_201_CREATED
        )

    except requests.exceptions.RequestException as e:
        print("Error creating new order: ",str(e))
        return get_error_response(HTTP_502_BAD_GATEWAY, str(e))

def update_order(orderId: str, request: OrderUpdate) -> BaseAPIResponse:
    try:
        update_data = request.model_dump(exclude_unset=True)
        response = requests.patch(baseUrl+"/orders/"+orderId, json=update_data)
        if response.status_code > 299:
            return get_error_response(response.status_code)
        response.raise_for_status()

        data = response.json()
        print("⬆️ Record Updated: ", data)      
        return success_response(
            message="✅ Record updated successfully!",
            data=data,
            status_code=HTTP_200_OK
        )
    
    except requests.exceptions.RequestException as e:
        print("Error updating record: ",str(e))
        return get_error_response(HTTP_502_BAD_GATEWAY)

def delete_order(orderId: str) -> BaseAPIResponse:
    try:
        response = requests.delete(baseUrl+"/orders/"+orderId)
        if response.status_code > 299:
            return get_error_response(response.status_code)
        response.raise_for_status()
        data = response.json()
        print("❌ Deleted Record: ", data)
        return success_response(
            message="✅ Record deleted successfully!",
            data=None,
            status_code=HTTP_200_OK
        )
    
    except requests.exceptions.RequestException as e:
        print("Deleting record failed "+str(e))
        return get_error_response(HTTP_502_BAD_GATEWAY)
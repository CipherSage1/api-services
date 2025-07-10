from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_502_BAD_GATEWAY
import requests

 
from user_order_app.error.error_handler import get_error_response
from user_order_app.utils.network_response import success_response
from user_order_app.models.order_model import Order
from user_order_app.models.base_response_model import BaseAPIResponse

baseUrl = "http://localhost:3000"
def get_all_orders() -> BaseAPIResponse:
    try:
        response = requests.get(baseUrl+"/orders")
        if response.status_code > 299:
            return get_error_response(response.status_code)
        response.raise_for_status()

        data = response.json()
        print("👨🏾‍🍳 Orders: ", data)
        return success_response(
            message="Request successful!",
            data={ "orders":   data },
            status_code=HTTP_200_OK
        )
    
    except requests.exceptions.RequestException  as e:
        print("Error fetching data:", str(e))
        return get_error_response(HTTP_502_BAD_GATEWAY)

def create_new_order(request: Order)  -> BaseAPIResponse:
    try:
        response = requests.post(baseUrl+"/orders", json=request.model_dump(mode="json"))
        if response.status_code > 299:
            return get_error_response(response.status_code)
        response.raise_for_status()

        data = response.json()
        print("🆕 Record: ", data)
        return success_response(
            message="Record created successfully!",
            data=data,
            status_code=HTTP_201_CREATED
        )

    except requests.exceptions.RequestException as e:
        print("Error creating new order: ",str(e))
        return get_error_response(HTTP_502_BAD_GATEWAY)

def update_order(orderId: str, request: Order) -> BaseAPIResponse:
    try:
        response = requests.patch(baseUrl+"/orders/"+orderId, json=request.model_dump(mode="json"))
        if response.status_code > 299:
            return get_error_response(response.status_code)
        response.raise_for_status()

        data = response.json()
        print("⬆️ Record Updated: ", data)      
        return success_response(
            message="Record updated successfully!",
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
            message="Record deleted successfully!",
            data=None,
            status_code=HTTP_200_OK
        )
    
    except requests.exceptions.RequestException as e:
        print("Deleting record failed "+str(e))
        return get_error_response(HTTP_502_BAD_GATEWAY)
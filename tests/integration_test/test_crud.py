from src.helpers.api_request_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_requests,put_requests,delete_requests
from src.helpers.utils import common_headers_json,common_headers_put
from src.helpers.payload_managers import payload_create_booking,payload_create_token
from src.helpers.comman_verification import verify_response_key_should_not_be_none,verify_http_status_code
import pytest


class TestCreateBooking(object):

    @pytest.fixture()
    def create_token(self):
        response = post_requests(
            url=APIConstants.url_create_token(self),
            auth=None,
            headers=common_headers_json(),
            payload=payload_create_token(),
            in_json=False
        )

        verify_http_status_code(response,200)
        token = response.json()["token"]
        print(token)
        verify_response_key_should_not_be_none(token)
        return token

    @pytest.fixture()
    def create_booking(self):
        response = post_requests(url=APIConstants.url_create_booking(self), auth=None, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, expected_data=200)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        return bookingid


    def test_update_booking(self,create_token,create_booking):#token and booking ID from the create booking. token
        bookingId = create_booking
        token = create_token
        put_url = APIConstants.url_create_booking(self) +"/"+str(bookingId)
        response = put_requests(
            url = put_url,
            auth=None,
            headers=common_headers_put(),
            payload=payload_create_booking(),
            in_json=False)

        print(response.json())



    def test_delete_booking(self,create_booking,create_token):
        bookingId = create_booking
        token = create_token
        delete_url = APIConstants.url_create_booking() +"/"+str(bookingId)
        response = delete_requests(url=delete_url,headers=common_headers_put(),payload=None,in_json=False)
        print(response.json())

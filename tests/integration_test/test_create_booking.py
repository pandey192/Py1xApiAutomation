from src.helpers.api_request_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_requests
from src.helpers.utils import common_headers_json
from src.helpers.payload_managers import payload_create_booking
from src.helpers.comman_verification import verify_response_key_should_not_be_none,verify_http_status_code
import pytest

class TestCreateBooking(object):
    @pytest.mark.positive
    def test_create_booking_tc1(self):
        response = post_requests(url=APIConstants.url_create_booking(self), auth=None, headers=common_headers_json(),payload=payload_create_booking(),in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response,expected_data=200)
        bookingid = response.json()["bookingid"]
        print(bookingid)

    @pytest.mark.negative
    def test_create_booking_tc2(self):
        response = post_requests(url=APIConstants.url_create_booking(self), auth=None, headers=common_headers_json(),payload={}, in_json=False)
        verify_http_status_code(response,expected_data=500)


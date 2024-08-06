import json
import os
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_requests
from src.helpers.comman_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_managers import payload_create_booking
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):

    def load_schema(self, schema_file):
        with open(schema_file, 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    def test_create_booking_tc1(self):
        response = post_requests(url=APIConstants.url_create_booking(self), auth=None, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, expected_data=200)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, expected_data=200)
        response_json = response.json()

        dir = os.getcwd()
        file = dir + "/schema.json"
        schema = self.load_schema(file)

        try:
           validate(instance=response_json, schema=schema)
        except ValidationError as e:
          print(e.message)

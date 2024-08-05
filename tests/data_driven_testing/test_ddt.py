#Read the CSV or excel file
#Create a function Create_token which can take values from the excel file
#Verify the expected result


#Read the Excel file
import sys
import openpyxl
import requests
import pytest
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json

#Step 1 Read the file
def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(url= "https://restful-booker.herokuapp.com/aut", headers=common_headers_json(), json=payload)
    return response

def test_post_create_token():
    file_path = "/Users/apple/PycharmProjects/Py1xApiAutomation/tests/data_driven_testing/testdata_ddt.xlsx"
    credentials = read_credentials_from_excel(file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = make_request_auth(username, password)
        print(response)
        assert response.status_code == 200


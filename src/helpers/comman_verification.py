#Https status verification


def verify_http_status_code(response_data,expected_data):
    print(response_data.status_code)
    assert response_data.status_code == expected_data, "Expcted HTTP status code" + str(expected_data)


def verify_json_key_for_not_null(key):
    assert key !=0, "Key is non Empty" + key
    assert key > 0, "Key is greater than zero"

#Comman verificatiomn
#HTTPS Status code
#Headers
#Data Verification
#Json Schema

def verify_response_key_should_not_be_none(key):
    assert key is not None

def verify_response_time():
    pass
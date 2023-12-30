# To make the post put patch delete

# HTTP methods -  Genric functions we will make

import requests
import json

def get_requests(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response

def post_requests(url,auth,headers,payload,in_json):
    post_response = requests.post(url=url, auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def patch_requests(url,auth,headers,payload, in_json):
    patch_response_data = requests.patch(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data

def put_requests(url,auth,headers,payload,in_json):
    put_response_data = requests.put(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return put_response_data.json()
    return put_response_data

def delete_requests(url,auth,headers,payload,in_json):
    delete_response_data = requests.delete(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data
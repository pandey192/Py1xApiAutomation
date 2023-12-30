#Comman headers


def common_headers_json():
    headers = {
        "Content-type": "application/json",
    }
    return headers

def common_headers_put():
    headers = {
        "Content-type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers


def common_headers_xml():
    headers = {
        "Content-Type": "application/xml",
    }
    return headers

# Read data from Excel ,csv ,json, YAML - keep the fucntions in future
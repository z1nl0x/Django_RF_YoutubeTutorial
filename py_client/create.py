import requests 

headers = {
    "Authorization": "Bearer 7beeb43c18642dae9c3d47284db37ba8202a1037"
}

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is the Tittle 99",
    "price": 52.31
}

# get_response = requests.post(endpoint)

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
print(get_response.status_code)
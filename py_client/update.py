import requests 


headers = {
    "Authorization": "Bearer 7beeb43c18642dae9c3d47284db37ba8202a1037"
}

endpoint = "http://localhost:8000/api/products/4/update/"

data = {
    "title": "Hello World Update Mixins 4",
    "price": 117.77
}

get_response = requests.put(endpoint, json=data, headers=headers)

print(get_response.json())
print(get_response.status_code)


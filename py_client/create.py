import requests 


endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is the Tittle 8",
    "price": 11.19
}

# get_response = requests.post(endpoint)

get_response = requests.post(endpoint, json=data)

print(get_response.json())
print(get_response.status_code)
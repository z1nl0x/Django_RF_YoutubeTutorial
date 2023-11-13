import requests 


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Hello World 1",
    "price": 129.99
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
print(get_response.status_code)


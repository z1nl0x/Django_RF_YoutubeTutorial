import requests 


endpoint = "http://localhost:8000/api/products/7/update/"

data = {
    "title": "Hello World Update Mixins 7",
    "price": 117.77
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
print(get_response.status_code)


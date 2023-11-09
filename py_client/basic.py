import requests 


# endpoint = "https://httpbin.org/status/200"

# endpoint = "https://httpbin.org/anything"

# endpoint = "https://httpbin.org/"

endpoint = "http://localhost:8000/api/"

# API -> Application Programming Interface

# get_response = requests.get(endpoint, params={"abc" : 123}, json={"product_id": 123})

# get_response = requests.get(endpoint, json={"product_id": 123})
get_response = requests.post(endpoint, json={"title": "abc", "content": "Hello World!", "price": "tralala"})

print(get_response.json())
print(get_response.status_code)

# get_response = requests.get(endpoint, data={"query": "Hello World!"})
# get_response = requests.get(endpoint, json={"query": "Hello World!"}) 
# print(get_response.json())
# print(get_response.status_code)
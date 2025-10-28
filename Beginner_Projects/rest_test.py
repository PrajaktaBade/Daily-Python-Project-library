import requests

url = "https://jsonplaceholder.typicode.com/users/1"  # test API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)

from urllib import response
import requests, json

BASE = "http://127.0.0.1:5001/"

data ={
    "username": "bill1",
    "pwd": "bill1"
}
#response = requests.put(BASE + "users", data)
response = requests.get(BASE + "users")
print(response.json())
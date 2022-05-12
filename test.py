from urllib import response
import requests, json

BASE = "http://localhost:5000/"

data ={
    "username": "bill1",
    "pwd": "bill1"
}
#response = requests.put(BASE + "users", data)
response = requests.get(BASE + "users")
print(response.json())
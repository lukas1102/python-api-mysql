from urllib import response
import requests, json

BASE = "http://172.16.0.10/"

data ={
    "username": "bill1",
    "pwd": "bill1"
}
#response = requests.put(BASE + "users", data)
response = requests.get(BASE)
print(response.json())
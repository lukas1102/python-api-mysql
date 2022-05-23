from urllib import response
import requests, json

BASE = "http://172.16.0.10/"

data ={
    "name1": "bill1",
    "name2": "bill1"
}
#response = requests.put(BASE, data)
response = requests.get(BASE)
print(response.json())
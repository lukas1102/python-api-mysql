from urllib import response
import requests, json

#BASE = "http://77.237.53.201:8113/"
#BASE = "http://localhost:5001/"
BASE = "http://172.16.0.10/"

response = requests.get(BASE)
print(response.json())
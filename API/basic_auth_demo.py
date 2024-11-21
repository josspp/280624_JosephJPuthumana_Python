import requests
from requests.auth import HTTPBasicAuth

url = "https://httpbin.org/basic-auth/user/pass"
auth = HTTPBasicAuth("user","pass")

response = requests.get(url,auth=auth)
print(response.json())

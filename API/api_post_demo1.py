import requests
import pandas as pd

url="https://jsonplaceholder.typicode.com/posts"

data={
    "title":"Rohits sessiosn", "body":"hello","userId":1
}

response =requests.post(url,json=data)

print(response.status_code)


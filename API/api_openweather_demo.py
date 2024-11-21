import requests
import pandas as pd

url="https://api.open-meteo.com/v1/forecast"

params={
    "latitude":12.9719 ,
    "longitude": 77.5937,
    "current_weather":"true"
}

response =requests.get(url,params)

print(response.json()['current_weather'])


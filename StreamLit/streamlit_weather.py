import requests
import time
import streamlit as st

st.title("Weather Demo")

lat=st.text_input("Latidude:")
long=st.text_input("Longitude:")

lat=float(lat)
long=float(long)
url="https://api.open.meteo.com/v1/forecast"

params = {
    "latitude":12.9719,
    "longitude":77.5937,
    "current_weather":"true"
}

response = requests.get(url,params)
#print(response)
#print(response.json(['current_weather']))
st.write(response.json()['current_weather']["temperature"])
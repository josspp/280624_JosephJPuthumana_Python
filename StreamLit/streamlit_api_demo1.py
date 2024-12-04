#import requests
#import time

#url="https://api.open.meteo.com/v1/forecast"

#params = {
#    "latitude":12.9719,
#    "longitude":77.5937,
#    "current_weather":"true"
#}

#response = requests.get(url,params)
#print(response)
#print(response.json(['current_weather']))


import streamlit as st
import requests

# Set up the Streamlit app title
st.title("Weather Forecast App")

# Add input fields for latitude and longitude (you can use default values or let the user input)
latitude = st.number_input("Enter latitude:", value=12.9719, format="%.2f")
longitude = st.number_input("Enter longitude:", value=77.5937, format="%.2f")

# API endpoint and parameters
url = "https://api.open.meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": "true"
}

# Get weather data when the user clicks the 'Get Weather' button
if st.button("Get Weather"):
    try:
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response and extract current weather data
            data = response.json()
            current_weather = data.get("current_weather", None)
            
            if current_weather:
                # Display current weather details
                temperature = current_weather.get("temperature", "N/A")
                wind_speed = current_weather.get("windspeed", "N/A")
                wind_direction = current_weather.get("winddirection", "N/A")
                weather_code = current_weather.get("weathercode", "N/A")
                
                # Display the extracted weather data
                st.subheader(f"Weather Details for Latitude: {latitude}, Longitude: {longitude}")
                st.write(f"Temperature: {temperature} °C")
                st.write(f"Wind Speed: {wind_speed} km/h")
                st.write(f"Wind Direction: {wind_direction}°")
                st.write(f"Weather Code: {weather_code}")
            else:
                st.error("Could not fetch weather data.")
        else:
            st.error(f"Error: Unable to fetch data (Status Code: {response.status_code})")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")

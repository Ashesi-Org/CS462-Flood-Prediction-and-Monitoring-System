import os
from dotenv import load_dotenv
import requests
import streamlit as st
from datetime import datetime

# Load environment variables from the .env file
load_dotenv()


# Access environment variables
openweather_api_key = os.getenv('OPENWEATHER_API_KEY')
st.write(f"API Key Loaded: {openweather_api_key}")
# Function to get weather data
def get_weather_data(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely&appid={openweather_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        st.write(f"API Response: {response.text}")
        return response.json()
    else:
        st.error(f"Error {response.status_code}: {response.json().get('message', 'Unknown error')}")
        return None


# Streamlit app interface
st.title('Weather Dashboard')
st.write("Enter your location coordinates:")

lat = st.number_input("Latitude", -90.0, 90.0, 37.7749)  # Default to San Francisco
lon = st.number_input("Longitude", -180.0, 180.0, -122.4194)  # Default to San Francisco

if st.button("Get Weather Data"):
    weather_data = get_weather_data(lat, lon)

    if weather_data:
        st.subheader("Current Weather Data")
        st.write(f"Temperature: {weather_data['current']['temp']} °C")
        st.write(f"Humidity: {weather_data['current']['humidity']}%")
        st.write(f"Cloudiness: {weather_data['current']['clouds']}%")
        st.write(f"Wind Speed: {weather_data['current']['wind_speed']} m/s")
        st.write(f"Wind Gusts: {weather_data['current'].get('wind_gust', 'Not available')} m/s")
        st.write(f"Precipitation in the last hour: {weather_data['current'].get('rain', {}).get('1h', 0)} mm")

        # Display hourly forecast for the next 12 hours
        st.subheader("Hourly Forecast (Next 12 Hours)")
        hourly_data = weather_data['hourly'][:12]
        for hour in hourly_data:
            time = datetime.utcfromtimestamp(hour['dt']).strftime('%Y-%m-%d %H:%M:%S')
            temp = hour['temp']
            rain = hour.get('rain', {}).get('1h', 0)
            st.write(f"Time: {time}, Temp: {temp}°C, Rain: {rain} mm")
    else:
        st.write("Could not fetch data. Please try again.")


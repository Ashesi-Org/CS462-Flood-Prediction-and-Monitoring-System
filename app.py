import streamlit as st
import requests
import pickle
import joblib
import numpy as np
from scipy.stats import norm

# OpenWeatherAPI Key (Replace with your key)
API_KEY = "105ce953cde35584a8658700b5a46803"

# Load the scaler and model
scaler_path = "scaler.pkl"
model_path = "logreg_model.pkl"

with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

model = joblib.load(model_path)


# Function to fetch weather data
def fetch_weather_data(city=None, lat=None, lon=None):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"appid": API_KEY, "units": "metric"}
    
    if city:
        params["q"] = city
    elif lat is not None and lon is not None:
        params["lat"] = lat
        params["lon"] = lon
    else:
        st.error("Please provide either a city name or coordinates.")
        return None

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        st.session_state['weather_data'] = response.json()
    else:
        st.error(f"Error fetching data: {response.status_code}")

# Function to display weather data
def display_weather_data(weather_data):
    st.subheader(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Temperature", f"{weather_data['main']['temp']}°C")
        st.metric("Min Temperature", f"{weather_data['main']['temp_min']}°C")
        st.metric("Max Temperature", f"{weather_data['main']['temp_max']}°C")
    with col2:
        st.metric("Pressure", f"{weather_data['main']['pressure']} hPa")
        st.metric("Humidity", f"{weather_data['main']['humidity']}%")
        st.metric("Weather", weather_data['weather'][0]['description'].title())

    icon_url = f"http://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}@2x.png"
    st.image(icon_url, caption=weather_data['weather'][0]['main'])

# Feature explanations and inputs
def flood_factors_input():
    features = {
        "Monsoon Intensity": "Rate the severity of monsoon rains in the region.",
        "Topography Drainage": "Evaluate the region's natural drainage capabilities.",
        "River Management": "Assess the quality of river management systems.",
        "Deforestation": "Rate the impact of deforestation on the area.",
        "Urbanization": "Rate the level of urbanization and its effect on water flow.",
        "Climate Change": "Assess the effect of climate change in the area.",
        "Dams Quality": "Rate the structural integrity and management of dams.",
        "Siltation": "Evaluate the extent of silt buildup in water bodies.",
        "Agricultural Practices": "Rate farming practices and their impact on flooding.",
        "Encroachments": "Rate the impact of illegal constructions on flood risk.",
        "Ineffective Disaster Preparedness": "Assess the region's disaster readiness.",
        "Drainage Systems": "Rate the efficiency of the drainage infrastructure.",
        "Coastal Vulnerability": "Rate the vulnerability of coastal areas to flooding.",
        "Landslides": "Assess the risk and impact of landslides in the region.",
        "Watersheds": "Evaluate the condition and management of watersheds.",
        "Deteriorating Infrastructure": "Rate the condition of essential infrastructure.",
        "Population Score": "Rate the population's density and its impact on flooding.",
        "Wetland Loss": "Rate the extent of wetland loss in the region.",
        "Inadequate Planning": "Evaluate urban planning and flood control measures.",
        "Political Factors": "Rate the impact of political decisions on flood risk."
    }

    st.subheader("Flood Risk Factors")
    inputs = {}
    for feature, explanation in features.items():
        st.markdown(f"**{feature}**: {explanation}")
        inputs[feature] = st.slider(f"Rate {feature}", min_value=0, max_value=10, step=1)
    return inputs

# Function to make prediction and calculate confidence interval
def predict_flood_risk(inputs):
    # Convert inputs dictionary to a list of values
    input_values = np.array(list(inputs.values())).reshape(1, -1)
    
    # Scale the inputs
    scaled_inputs = scaler.transform(input_values)

    # Make prediction
    prediction = model.predict(scaled_inputs)[0]
    proba = model.predict_proba(scaled_inputs)[0]

    # Confidence interval (assuming a normal distribution of probabilities)
    mean_proba = proba.max()
    std_dev = np.std(proba)
    confidence_interval = norm.interval(0.95, loc=mean_proba, scale=std_dev)
    lower_bound = max(0, confidence_interval[0])
    upper_bound = min(1, confidence_interval[1])
    st.write(f"Confidence Interval (95%): {lower_bound:.2%} to {upper_bound:.2%}")

    return prediction, mean_proba, lower_bound, upper_bound



# Main App
st.title("Flood Prediction and Monitoring System")

menu = ["History", "Predict Flood", "Learn About Your Community"]
choice = st.sidebar.selectbox("Navigate", menu)

if choice == "Predict Flood":
    st.header("Predict Flood Risk")
    
    if "weather_data" not in st.session_state:
        st.session_state["weather_data"] = None

    option = st.radio("Select input method:", ("City Name", "Coordinates"))

    if option == "City Name":
        city = st.text_input("Enter City Name")
        if st.button("Fetch Weather Data"):
            fetch_weather_data(city=city)

    elif option == "Coordinates":
        lat = st.number_input("Enter Latitude", format="%.4f")
        lon = st.number_input("Enter Longitude", format="%.4f")
        if st.button("Fetch Weather Data"):
            fetch_weather_data(lat=lat, lon=lon)

    if st.session_state["weather_data"]:
        display_weather_data(st.session_state["weather_data"])
        st.write("---")

        user_inputs = flood_factors_input()

        if st.button("Predict Flood Risk"):
            prediction, mean_proba, lower_bound, upper_bound = predict_flood_risk(user_inputs)

            if prediction == 1:
                st.success(f"Flood Risk Predicted! Probability: {mean_proba:.2%}")
            else:
                st.info(f"No Flood Risk Predicted. Probability: {mean_proba:.2%}")

            st.write(f"Confidence Interval (95%): {lower_bound:.2%} to {upper_bound :.2%}")

elif choice == "History":
    st.header("History")
    st.write("This section will display historical data and trends.")

elif choice == "Learn About Your Community":
    st.header("Learn About Your Community")
    st.write("This section will provide educational resources and community updates.")

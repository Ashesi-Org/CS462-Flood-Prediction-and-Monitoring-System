from flask import Flask, jsonify, request, render_template
import requests
from dotenv import load_dotenv
import os
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS
API_KEY_2 = os.getenv("ROBUST_API_KEY")
API_KEY = os.getenv("WEATHER_API_KEY")

ROBUST_API_URL = "https://payload.vextapp.com/hook/O0WKVBXQE4/catch/user"
HEADERS = {"Content-Type": "application/json", "ApiKey": f"Api-Key {API_KEY_2}"}

# Function to fetch weather data
def fetch_weather_data(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

# Home route that renders index.html
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# API route to fetch weather data
@app.route("/api/weather", methods=["GET"])
def get_weather():
    city = request.args.get("location")
    if not city:
        return jsonify({"error": "Location not provided"}), 400

    weather_data = fetch_weather_data(city)
    if not weather_data:
        return jsonify({"error": "Unable to fetch weather data"}), 500

    risk_level = "High" if weather_data["main"]["humidity"] > 70 else "Low"

    return jsonify({
        "city": weather_data["name"],
        "country": weather_data["sys"]["country"],
        "temperature": weather_data["main"]["temp"],
        "weather": weather_data["weather"][0]["description"],
        "flood_probability": weather_data["main"]["humidity"],
        "risk_level": risk_level,
    })

@app.route('/result', methods=['GET'])
def result():
    # Extract query parameters
    flood_probability = request.args.get('flood_probability')
    lower_bound = request.args.get('lower_bound')
    upper_bound = request.args.get('upper_bound')

    # Convert to float (if valid)
    try:
        flood_probability = float(flood_probability)
        lower_bound = float(lower_bound)
        upper_bound = float(upper_bound)
    except ValueError:
        return "Invalid input values provided", 400  # Return an error if conversion fails

    # Render the results page
    return render_template(
        'result.html',
        flood_probability=flood_probability,
        lower_bound=lower_bound,
        upper_bound=upper_bound
    )

# Route to render the flood risk evaluation form
@app.route("/evaluation-form", methods=["GET"])
def evaluation_form():
    return render_template("predictflood.html")

# Route to handle form submission
@app.route("/submit-evaluation", methods=["POST"])
def submit_evaluation():
    data = request.form
    # Extract and process form inputs
    scores = {key: int(value) for key, value in data.items() if value.isdigit()}

    # Basic example of a weighted scoring system
    total_score = sum(scores.values())
    average_score = total_score / len(scores)
    flood_risk = "High" if average_score > 70 else "Medium" if average_score > 40 else "Low"

    return jsonify({
        "total_score": total_score,
        "average_score": average_score,
        "flood_risk": flood_risk
    })
@app.route("/comprehensive-analysis")
def comprehensive_analysis():
    data = {
        "payload": "Hey there I live in Kasoa Nyanyano, tell me whether there would be flood today"
    }

    try:
        # Call the API
        response = requests.post(ROBUST_API_URL, headers=HEADERS, json=data)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

        # Ensure the request was successful
        response.raise_for_status()
        analysis_data = response.json()

        # Pass the entire response to the template
        return render_template("simplified_analysis.html", data={"response": analysis_data})

    except requests.exceptions.RequestException as e:
        # Handle API errors gracefully
        error_message = f"Failed to fetch analysis: {str(e)}"
        print(error_message)  # Log for debugging
        return render_template("simplified_analysis.html", data={"error": error_message}), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

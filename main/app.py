from flask import Flask, jsonify, request, redirect
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)# Enable CORS

# Endpoint to interact with the localmodelapi container
LOCAL_MODEL_API_URL = "http://127.0.0.1:5000/predict_flood"  # Container name used as hostname

@app.route("/flood-prediction", methods=["POST"])
def flood_prediction():
    data = request.json
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Forward the POST request to localmodelapi
    try:
        response = requests.post(LOCAL_MODEL_API_URL, json=data)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error communicating with localmodelapi: {str(e)}"}), 500


# Redirect requests to the user-prediction-api container
@app.route("/")
def home():
    # Forward the request to the user-prediction-api container's homepage
    return redirect("http://127.0.0.1:5001/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)

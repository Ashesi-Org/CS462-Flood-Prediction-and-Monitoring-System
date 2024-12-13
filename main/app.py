from flask import Flask, jsonify, request, redirect
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# External service URLs
FLOOD_PREDICTION_API_URL = "http://127.0.0.1:5000/predict_flood"  # Flood prediction service
LANDING_PAGE_URL = "http://127.0.0.1:8000/landing"  # Landing page service
USER_PREDICTION_API_URL = "http://127.0.0.1:5001/"  # User prediction service
# USER_HISTORY_API_URL = "http://127.0.0.1:7000/user_history"  # User history service

# ============================
# API Endpoints
# ============================

@app.route("/")
def home():
    """
    Redirect to the landing page.
    """
    return redirect(LANDING_PAGE_URL)

@app.route("/details")
def details():
    """
    Redirect to the user-prediction-api homepage.
    """
    return redirect(USER_PREDICTION_API_URL)

@app.route("/flood-prediction", methods=["POST"])
def flood_prediction():
    """
    Forward flood prediction requests to the flood prediction service.
    """
    data = request.json
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        response = requests.post(FLOOD_PREDICTION_API_URL, json=data)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error communicating with flood prediction API: {str(e)}"}), 500

# @app.route("/user-history", methods=["GET"])
# def user_history():
#     """
#     Forward requests to fetch user history to the user-history service.
#     """
#     try:
#         user_id = request.args.get("user_id")
#         params = {"user_id": user_id} if user_id else {}
#         response = requests.get(USER_HISTORY_API_URL, params=params)
#         response.raise_for_status()
#         return jsonify(response.json()), response.status_code
#     except requests.exceptions.RequestException as e:
#         return jsonify({"error": f"Error communicating with user history API: {str(e)}"}), 500

# ============================
# Application Entry Point
# ============================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

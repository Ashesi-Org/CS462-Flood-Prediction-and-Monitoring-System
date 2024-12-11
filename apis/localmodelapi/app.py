from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import joblib
import os
from flask_cors import CORS



# Initialize Flask app
app = Flask(__name__)

CORS(app) 


# Load the pre-trained model
MODEL_PATH = "flood_model.h5"
# MODEL_PATH = "../models/flood_model.h5"

if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH, custom_objects={"mse": tf.keras.losses.MeanSquaredError()})
else:
    raise FileNotFoundError("The flood_model.h5 file was not found!")

# Load the scaler
SCALER_PATH = "scaler.pkl"
# SCALER_PATH = "../models/scaler.pkl"

if os.path.exists(SCALER_PATH):
    scaler = joblib.load(SCALER_PATH)
else:
    raise FileNotFoundError("The scaler.pkl file was not found!")

# Expected feature names (in correct order)
FEATURE_NAMES = [
    "Monsoon Intensity", "Topography Drainage", "River Management",
    "Deforestation", "Urbanization", "Climate Change",
    "Dams Quality", "Siltation", "Agricultural Practices",
    "Encroachments", "Ineffective Disaster Preparedness",
    "Drainage Systems", "Coastal Vulnerability", "Landslides",
    "Watersheds", "Deteriorating Infrastructure", "Population Score",
    "Wetland Loss", "Inadequate Planning", "Political Factors"
]

@app.route('/predict_flood', methods=['POST'])
def predict_flood():
    try:
        # Parse input JSON data
        input_data = request.json
        if not input_data:
            return jsonify({"error": "No input data provided"}), 400

        # Check for missing features
        missing_features = [f for f in FEATURE_NAMES if f not in input_data]
        if missing_features:
            return jsonify({"error": f"Missing features: {missing_features}"}), 400

        # Ensure input values are in the correct order
        try:
            input_values = [float(input_data[feature]) for feature in FEATURE_NAMES]
        except ValueError as e:
            return jsonify({"error": f"Invalid input data: {e}"}), 400

        # Convert to NumPy array and reshape for the model
        input_array = np.array(input_values).reshape(1, -1)

        # Apply the scaler
        scaled_input = scaler.transform(input_array)

        # Make prediction
        prediction = model.predict(scaled_input)
        flood_probability = float(prediction[0][0])

        # Calculate a simple confidence interval (example: ±5%)
        confidence_interval_margin = 0.05  # Adjust as needed
        lower_bound = max(0.0, flood_probability - confidence_interval_margin)
        upper_bound = min(1.0, flood_probability + confidence_interval_margin)

        # Create response
        response = {
            "flood_probability": flood_probability,
            "confidence_interval": {
                "lower_bound": lower_bound,
                "upper_bound": upper_bound
            }
        }

        return jsonify(response), 200

    except Exception as e:
        # Log the exception for debugging
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import joblib
import os
import scipy.stats as stats

app = Flask(__name__)

# Load the pre-trained model
if os.path.exists("models/flood_model.h5"):
    model = tf.keras.models.load_model("models/flood_model.h5", custom_objects={"mse": tf.keras.losses.MeanSquaredError()})
else:
    raise FileNotFoundError("The flood_model.h5 file was not found!")

# Load the scaler (only once)
scaler = joblib.load('models/scaler.pkl')  # Adjust path as needed

# Define the route for flood prediction
@app.route('/predict_flood', methods=['POST'])
def predict_flood():
    try:
        # Parse JSON data from request
        input_data = request.json

        # Ensure input_data is in the expected order of features
        feature_names = [
            "Monsoon Intensity", "Topography Drainage", "River Management",
            "Deforestation", "Urbanization", "Climate Change",
            "Dams Quality", "Siltation", "Agricultural Practices",
            "Encroachments", "Ineffective Disaster Preparedness",
            "Drainage Systems", "Coastal Vulnerability", "Landslides",
            "Watersheds", "Deteriorating Infrastructure", "Population Score",
            "Wetland Loss", "Inadequate Planning", "Political Factors"
        ]

        # Convert input JSON to list of values in the correct order
        input_values = [input_data[feature] for feature in feature_names]

        # Convert to NumPy array and reshape for scaler
        input_array = np.array(input_values).reshape(1, -1)

        # Apply the scaler to the input
        scaled_input = scaler.transform(input_array)  # Use scaler's transform method

        # Make prediction
        prediction = model.predict(scaled_input)

        # Convert prediction (numpy.float32) to a standard Python float for JSON serialization
        flood_probability = float(prediction[0][0])

        # Calculate the confidence interval
        # Let's assume we use a 95% confidence interval (for example) and a normal distribution
        # In practice, you could calculate the standard deviation of model predictions
        # if you have multiple predictions or use dropout at inference time.

        # For now, let's estimate a simple margin based on a normal distribution
        confidence_interval_margin = 0.05  # Example margin, you can adjust this based on your model's uncertainty

        lower_bound = flood_probability - confidence_interval_margin
        upper_bound = flood_probability + confidence_interval_margin

        # Create response with confidence interval
        response = {
            "flood_probability": flood_probability,
            "confidence_interval": {
                "lower_bound": lower_bound,
                "upper_bound": upper_bound
            }
        }

        return jsonify(response), 200

    except KeyError as e:
        return jsonify({"error": f"Missing feature in input data: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

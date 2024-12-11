from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/flood-prediction')
def flood_prediction():
    # Logic to interact with flood-prediction-api service
    response = requests.get('http://flood-prediction-frontend:5000')
    return render_template('flood_prediction_result.html', result=response.json())

@app.route('/user-prediction')
def user_prediction():
    # Logic to interact with user-prediction-api service
    response = requests.get('http://user-prediction-frontend:5001')
    return render_template('user_prediction_result.html', result=response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

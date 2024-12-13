import requests

url = "http://127.0.0.1:5000/predict_flood"
headers = {"Content-Type": "application/json"}
data = {
    "Monsoon Intensity": 0.8,
    "Topography Drainage": 0.6,
    "River Management": 0.7,
    "Deforestation": 0.4,
    "Urbanization": 0.9,
    "Climate Change": 0.8,
    "Dams Quality": 0.5,
    "Siltation": 0.6,
    "Agricultural Practices": 0.7,
    "Encroachments": 0.3,
    "Ineffective Disaster Preparedness": 0.5,
    "Drainage Systems": 0.6,
    "Coastal Vulnerability": 0.4,
    "Landslides": 0.2,
    "Watersheds": 0.7,
    "Deteriorating Infrastructure": 0.6,
    "Population Score": 0.8,
    "Wetland Loss": 0.9,
    "Inadequate Planning": 0.4,
    "Political Factors": 0.5
}

response = requests.post(url, json=data, headers=headers)

print("Response status code:", response.status_code)
print("Response JSON:", response.json())

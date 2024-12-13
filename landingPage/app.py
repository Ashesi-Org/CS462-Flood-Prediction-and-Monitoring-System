from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/landing")
def landing():
    return render_template('landing.html')  # This will render your HTML file

@app.route("/frontend")
def frontend():
    return render_template('frontend.html')

@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)



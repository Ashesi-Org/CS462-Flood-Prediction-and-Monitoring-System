from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

<<<<<<< HEAD
=======
<<<<<<< HEAD
@app.route("/landing")
def landing():
    return render_template('landing.html')  # This will render your HTML file

@app.route("/frontend")
def frontend():
    return render_template('frontend.html')

@app.route("/login")
=======
>>>>>>> 42fa128fc2baa9d0cb0a6184d0166457365ed85d
@app.route('/', methods=["GET"])
def landing():
    return render_template('landing.html')  # This will render your HTML file

@app.route('/Frontend')
def frontend():
    return render_template('Frontend.html')

@app.route('/login')
<<<<<<< HEAD
=======
>>>>>>> b36831172537fc728081297df0e16a8108f2a883
>>>>>>> 42fa128fc2baa9d0cb0a6184d0166457365ed85d
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)



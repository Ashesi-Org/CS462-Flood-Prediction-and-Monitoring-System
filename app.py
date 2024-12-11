from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')  # This will render your HTML file

@app.route('/Frontend')
def frontend():
    return render_template('Frontend.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)



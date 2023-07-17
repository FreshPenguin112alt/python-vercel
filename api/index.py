from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome To The FROP API'

@app.route('/about')
def about():
    return 'About'

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome To The FROP API'

@app.route('/api/v1', methods=["POST"])
def about():
  if not request.get_json(force=True)["code"] == None:
    return request.get_json(force=True)["code"]
  else:
    return "Hello, World!"
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome To The FROP API'

@app.route('/api/v1', methods=["POST"])
def about():
  if not None == request.get_json(force=True).get("code"):
    return request.get_json(force=True).get("code")
  else:
    return "Hello, World!"
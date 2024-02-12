from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello_world():
    data = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }   
    return json.dumps(data)

@app.route("/hello")
def hello():
    return "<h1>Hello World</h1>"

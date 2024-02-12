from flask import Flask, jsonify
import requests
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

@app.route("/getinfo", methods=["GET"])
def getInfo():  
    response = requests.get("http://127.0.0.1:5000/")
    data = response.json()
    print(data)
    return f"<p>{data}</p>"
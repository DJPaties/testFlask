from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route("/getinfo", methods=["GET"])
def getInfo():  
    response = requests.get("http://127.0.0.1:5000/")
    data = response.json()
    print(data)
    return f"<p>{data}</p>"
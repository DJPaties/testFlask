from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello_world():
    data = {
    "success": True,
    "audioName": "https://test-flask-git-main-mdhost.vercel.app/static/audio.wav",
    }   
    return json.dumps(data)

@app.route("/hello")
def hello():
    return "<h1>Hello World</h1>"

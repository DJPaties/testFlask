from flask import Flask,request
import json
import TTSfunctions
import api.chatbot.chatcopy as ch


app = Flask(__name__)

@app.route("/")
def hello_world():
    data = {
    "success": True,
    "audio_name": "https://test-flask-git-main-mdhost.vercel.app/static/audio.wav",
    }   
    return json.dumps(data)

@app.route("/hello")
def hello():
    return "<h1>Hello World</h1>"



@app.route("/json-receive")
def get_json():
    return "JSON IS RECEIVED"
@app.route("/api/audio",methods=['POST'])
def get_audio():
    if request.method =="POST":
        x = request.files['messageFile']
        x.save("api/static/received.wav")
        print(request.files['messageFile'])
    x = TTSfunctions.transcribe_audio_wav("en")
    x = ch.receive_message(x)
    print(x)
    return x  


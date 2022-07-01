from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/salam/")
def hello_world_salam():
    return "<p>Hello, World salam!</p>"

from flask import Flask

app = Flask(__name__)

@app.route("/")
def get():
    return "Hello world from serve-1"

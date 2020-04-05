from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "Hello, world"

@app.route("/login", methods=["POST"])
def login():
    pass
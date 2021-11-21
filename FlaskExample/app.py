from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, from my first docker app :)</p>"


@app.route("/hi")
def hi_again():
    return "<p>Hi again</p>"

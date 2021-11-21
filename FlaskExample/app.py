import os
from flask import Flask, render_template

app = Flask(__name__)

# use: "> export APP_NAME=MrSpock; python app.py"
# in docker image/container: "> docker run -e APP_NAME=Scotty image_name-name"
star_trek = os.environ.get('APP_NAME')


@app.route("/")
def main():
    # return render_template('index.html', color="blue")
    return render_template('index.html', app_name=star_trek)


@app.route("/hello")
def hello():
    return "<p>Hello, from my first docker app :)</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

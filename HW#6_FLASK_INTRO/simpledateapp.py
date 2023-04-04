from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def date_time_printer():
    return f"<h1>{datetime.now()}</h1>"


if __name__ == "__main__":
    app.run('localhost', port=9000)

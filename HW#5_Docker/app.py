from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! gggggggtest1234567890!!!</p>"


app.run(host="0.0.0.0", port=5000, debug=True)
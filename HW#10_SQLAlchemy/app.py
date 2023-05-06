from flask import Flask, render_template, request, redirect, session
from models import User
from models import db


app = Flask(__name__)
##CREATE DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tinder_an.db"
db.init_app(app)


@app.route("/")
def index():
    return "Hello!"


@app.route("/login")
def login():
    pass


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/save-user", methods=["POST"])
def save_user():
    """
    Registration of the new user
    """
    data = request.form
    new_user = User(
        full_name=data.get("full_name"),
        age=data.get("age"),  # need validation!
        email=data.get("email"),  # need validation!
        password=data.get("password"),  ##need sha!
        gender=data.get("gender"),
    )

    db.session.add(new_user)
    db.session.commit()
    return redirect("/")


@app.route("/profile")
def profile():
    """
    User profile page
    """
    return render_template("profile.html")


@app.route("/matches")
def matches():
    pass


@app.route("/settings")
def settings():
    pass


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # create tables if do not exist

    app.run(host="localhost", port=5000, debug=True)

import hashlib
from app import app, db
from flask import render_template, request, redirect, session
from models import User, Post



@app.route("/")
def hello_world():
    posts = db.session.query(Post).all()
    posts = [post.serialize for post in posts]
    users_with_posts = db.session.query(User).join(User.posts).all()
    users_with_posts = [user.serialize for user in users_with_posts]
    return render_template("index.html", posts=posts, users=users_with_posts)


@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")


@app.route("/save-user", methods=["POST"])
def register():
    data = request.form
    password_hash = hashlib.sha256(data.get("password").encode("utf-8"))
    user = User(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        password=password_hash.hexdigest(),
    )
    db.session.add(user)
    db.session.commit()
    session["user"] = user.serialize
    return redirect("/")


@app.route("/sign-in")
def sign_in():
    return render_template("sign-in.html")


@app.route("/authorize", methods=["POST"])
def authorize():
    data = request.form
    user = User.query.filter(User.email == data.get("email")).first()
    if user:
        if hashlib.sha256(data.get("password").encode("utf-8")).hexdigest() == user.password:
            session["user"] = user.serialize
    return redirect("/")


@app.route("/logout")
def logout():
    del session["user"]
    return redirect("/")



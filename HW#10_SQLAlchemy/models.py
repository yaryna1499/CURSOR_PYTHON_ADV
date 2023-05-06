from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    descr = db.Column(db.Text, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    register_time = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(32), nullable=False)
    gender = db.Column(db.String(5), nullable=False)

    children = db.relationship("UserPhoto", backref="user", lazy=True)


class UserPhoto(db.Model):
    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True
    )  # forgot to create PKs in the schema!
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    img = db.Column(db.String, nullable=False)


# I Hope I`ll do it later!
class Location:
    pass


class Interaction:
    pass


class Message:
    pass


class UserSettings:
    pass


# Debugging:

if __name__ == "__main__":
    from flask import Flask

    dummyapp = Flask(__name__)
    dummyapp.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
    db.init_app(dummyapp)

    # Trick Flask into thinking we're into app context
    # to experement in interactive session
    ctx = dummyapp.app_context()

    # normally used as:
    # with app.app_context():
    #     db.create_all()
    #     ...
    ctx.__enter__()

    db.create_all()

    test_user = User(
        full_name="Test User",
        age=18,
        email="test@gmail.com",
        password="passwordTest",
        gender="Male",
    )

    test_img = UserPhoto(user_id=1, img="image object")

    db.session.add(test_user)
    db.session.add(test_img)
    db.session.commit()

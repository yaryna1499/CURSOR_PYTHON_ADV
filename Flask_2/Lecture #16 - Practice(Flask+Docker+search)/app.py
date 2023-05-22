from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flask:flask@db:3306/flask"
app.secret_key = "sadasdsdssadsadsadsadsadssaddas"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

# Import routes after initializing migration
from routes import *

if __name__ == "__main__":
    # Create tables in DB if not exist
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5050, debug=True)

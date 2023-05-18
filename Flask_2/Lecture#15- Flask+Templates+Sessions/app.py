from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/BlogDB"
app.secret_key = "sadasdsdssadsadsadsadsadssaddas"
db.init_app(app)

# Initialize migration
migrate = Migrate(app, db)

# Set app context before operations with DB
app.app_context().push()

# Import routes and after setting app context
from routes import *

# Create tables in DB if not exist
db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

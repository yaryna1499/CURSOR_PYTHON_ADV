from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/flask1"
app.secret_key = "sadasdsdssadsadsadsadsadssaddas"
db.init_app(app)

# Опціонально: ініціалізувати migrate
# migrate = Migrate(app, db)

# Додати app context перед виконанням операцій з БД
app.app_context().push()

# Імпортувати роути та моделі після встановлення app context
from routes import *
from models import User

# Створити таблиці в БД, якщо вони ще не існують
db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

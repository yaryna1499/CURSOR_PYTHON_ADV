from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    register_time = db.Column(db.DateTime, default=datetime.utcnow())
    logg_status = db.Column(db.Boolean, default=False)
    posts = db.relationship("Post", backref="user")


    def sign_in(self, id):
        self.logg_status = True
        db.session.commit()

    def log_out(self, id):
        self.logg_status = False
        db.session.commit()

    @property
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "logg_status": self.logg_status
        }
    


class Post(db.Model):
    __tablename__ = "posts"
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_datetime = db.Column(db.String(255), default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    post_header = db.Column(db.String(255), nullable=True)
    post_text = db.Column(db.Text, nullable=False)
    time_edited = db.Column(db.String(255), default=post_datetime)


    def edit_post(self, new_header, new_text):
        self.post_header = new_header
        self.post_text = new_text
        self.time_edited = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        db.session.commit()


    @property
    def serialize(self):
        return {
            "post_id": self.post_id,
            "user_id": self.user_id,
            "post_datetime": self.post_datetime,
            "post_header": self.post_header,
            "post_text": self.post_text,
            "time_edited": self.time_edited,
        }
    

class MenuItem(db.Model):
    __tablename__="menu_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "link": self.link
        }
    




"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


#USER model for Blogly
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        user = self
        return f"<user_id={user.id} firstname={user.first_name} lastname={user.last_name} image_url={user.image_url}>"

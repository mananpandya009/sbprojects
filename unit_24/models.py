"""Models for Pet"""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


#USER model for Blogly
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer ,primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        pet = self
        return f"<pet_id={pet.id} name={pet.name} species={pet.species} photo_url={pet.photo_url} age={pet.age} notes={pet.notes} available={pet.available}>"
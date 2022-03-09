"""Blogly application."""
from crypt import methods
from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm,EditPetForm
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "yoyo"
debug = DebugToolbarExtension(app)
connect_db(app)


@app.route('/')
def home():
    """blogly routes"""
    return redirect('/pets')


@app.route('/pets')
def list_pets():
    """blogly routes"""
    pets = Pet.query.all()
    return render_template('pet-list.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm();
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        
        new_pet = Pet(name=name, species=species, photo_url=photo_url,age=age,notes=notes,available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new-pet.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_edit_pet(pet_id):
    form = EditPetForm();
    pet = Pet.query.get_or_404(pet_id)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        return render_template('pet-details.html', form=form,pet=pet)



if __name__ == '__main__':
    app.run()
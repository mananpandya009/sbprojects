"""Blogly application."""
from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "yoyo"
debug = DebugToolbarExtension(app)
connect_db(app)


@app.route('/')
def home():
    """blogly routes"""
    return redirect(f'/users')


@app.route('/users')
def list_users():
    """blogly routes"""
    users = User.query.all()
    return render_template('user-list.html', users=users)



@app.route('/users/new')
def add_user_form():
    """blogly routes"""
    return render_template('new-user-form.html')


@app.route('/users/new', methods=['POST'])
def create_user():
    """blogly routes"""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    
    new_user  = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f'/users')
    

@app.route("/<int:user_id>")
def show_user(user_id):
    """blogly routes"""
    user = User.query.get_or_404(user_id)
    return render_template("user-details.html", user=user)


@app.route("/users/<int:user_id>/edit")
def edit_user_form(user_id):
    """blogly routes"""
    user = User.query.get_or_404(user_id)
    return render_template("edit-user-form.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=['POST'])
def edit_user_update_db(user_id):
    """blogly routes"""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    
    if first_name and last_name and image_url:
        edit_user = User.query.get_or_404(user_id)
        edit_user.first_name = first_name
        edit_user.last_name = last_name
        edit_user.image_url = image_url
        db.session.add(edit_user)
        db.session.commit()
        return redirect(f'/users')
    else:
        return redirect(f'/users/{user_id}/edit')


@app.route("/users/<int:user_id>/delete", methods=['POST'])
def delete_user_update_db(user_id):
    """blogly routes"""
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect(f'/users')



if __name__ == '__main__':
    app.run()
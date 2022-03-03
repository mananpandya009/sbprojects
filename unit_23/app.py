"""Blogly application."""
from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag
import datetime

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
    posts = user.posts
    return render_template("user-details.html", user=user, posts=posts)


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
    edit_user = User.query.get_or_404(user_id)
    if first_name:
        edit_user.first_name = first_name
    if last_name:
        edit_user.last_name = last_name
    if image_url:
        edit_user.image_url = image_url
              
    db.session.add(edit_user)
    db.session.commit()
    return redirect(f'/{edit_user.id}')



@app.route("/users/<int:user_id>/delete")
def delete_user_update_db(user_id):
    """blogly routes"""
    delete_user = User.query.get_or_404(user_id)
    db.session.delete(delete_user)
    db.session.commit()

    return redirect(f'/users')


@app.route('/users/<int:user_id>/posts/new')
def add_new_post_form(user_id):
    tags = Tag.query.all()
    return render_template('new-post-form.html', user_id=user_id,tags=tags )


@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def save_new_post(user_id):
    title = request.form["title"]
    content = request.form["content"]
    created_at = datetime.datetime.now().strftime("%H:%M:%S %m-%d-%Y")
    tag_list = request.form.getlist("tagname")


    if title and content:
        tags = Tag.query.filter(Tag.id.in_(tag_list)).all()
        new_post  = Post(title=title, content=content, created_at = created_at, user_id = user_id, tags=tags)
        db.session.add(new_post)
        db.session.commit()
        return redirect(f'/{user_id}')
    else:
        return redirect(f'/users/{user_id}/posts/new')


@app.route('/posts/<int:post_id>')
def show_post_details(post_id):
    post = Post.query.get_or_404(post_id)
    author = f'{post.user.first_name} {post.user.last_name}'
    tags = post.tags
    return render_template('post-details.html', post=post, author=author, tags=tags)


@app.route('/posts/<int:post_id>/edit')
def show_edit_post_form(post_id):
    post = Post.query.get_or_404(post_id)
    tags_used = post.tags
    tags = Tag.query.all()
    return render_template('edit-post-form.html', post=post, tags=tags, tags_used=tags_used)


@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_post_details(post_id):
    title = request.form["title"]
    content = request.form["content"]
    created_at =  datetime.datetime.now().strftime("%H:%M:%S %m-%d-%Y")
    edit_post = Post.query.get_or_404(post_id)
    tag_list = request.form.getlist("tagname")
    tags = Tag.query.filter(Tag.id.in_(tag_list)).all()

    if title:
        edit_post.title = title
        edit_post.created_at = created_at
    if content:
        edit_post.content = content
        edit_post.created_at = created_at
    if tag_list:
        edit_post.tags = tags
        edit_post.created_at = created_at


    db.session.add(edit_post)
    db.session.commit()
    return redirect(f'/posts/{edit_post.id}')


@app.route('/posts/<int:post_id>/delete')
def delete_post(post_id):
    delete_post = Post.query.get_or_404(post_id)
    db.session.delete(delete_post)
    db.session.commit()
    return redirect(f'/{delete_post.user_id}')


@app.route('/tags')
def show_tags_list():
    tags = Tag.query.all()
    return render_template('tags-list.html', tags=tags)


@app.route('/tags/new')
def show_new_tag_form():
    return render_template('new-tag-form.html')



@app.route('/tags/new',methods=['POST'])
def process_new_tag():
    name=request.form["tagname"]
    if name:
        new_tag  = Tag(name=name)
        db.session.add(new_tag)
        db.session.commit()
        return redirect(f'/tags')
    else:
        return redirect(f'/tags/new')


@app.route('/tags/<int:tag_id>')
def show_tag_details(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    posts = tag.posts
    return render_template('tag-details.html', posts=posts, tag=tag)



@app.route('/tags/<int:tag_id>/edit')
def show_edittag_form(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    tagged_posts = tag.posts
    posts = Post.query.all()
    return render_template('edit-tag-form.html',tag=tag, tagged_posts=tagged_posts, posts=posts)


@app.route('/tags/<int:tag_id>/edit', methods=['POST'])
def process_edittag_form(tag_id):
    edittag = Tag.query.get_or_404(tag_id)
    post_list = request.form.getlist("post")
    posts = Post.query.filter(Post.id.in_(post_list)).all()
    name=request.form["tagname"]
    if name:
        edittag.name = name 
        db.session.add(edittag)
        db.session.commit()
        return redirect(f'/tags')
    if post_list:
        edittag.posts = posts 
        db.session.add(edittag)
        db.session.commit()
        return redirect(f'/tags')
    else:
        return redirect(f'/tags/{tag_id}/edit')



@app.route('/tags/<int:tag_id>/delete')
def delete_tag(tag_id):
    delete_tag = Tag.query.get_or_404(tag_id)
    if delete_tag.posts:
        posts = delete_tag.posts
        tag = delete_tag
        return render_template('tag-details.html', posts=posts, tag=tag)
    else:
        db.session.delete(delete_tag)
        db.session.commit()
    return redirect(f'/tags')




if __name__ == '__main__':
    app.run()
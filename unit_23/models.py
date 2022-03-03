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


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id', ondelete='CASCADE'))
    user = db.relationship( 'User', backref='posts')
    # direct navigation: post -> tag & back
    exit
    tags = db.relationship('Tag',secondary='posttags',backref='posts')
    tagposts = db.relationship( 'PostTag', backref='posts')


    def __repr__(self):
        post = self
        return f"<post_id={post.id} post_title={post.title} post-content={post.content} created_at={post.created_at}>"

   


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    # direct navigation: tag -> posttag & back
    tag_post = db.relationship( 'PostTag', backref='tags')
    def __repr__(self):
        tag = self
        return f"<tag_id={tag.id} tagname={tag.name}>"
    




class PostTag(db.Model):
    __tablename__ = 'posttags'

    post_id = db.Column(db.Integer,db.ForeignKey('posts.id', ondelete='CASCADE'),primary_key=True)
    tag_id = db.Column(db.Integer,db.ForeignKey('tags.id', ondelete='CASCADE'),primary_key=True)  
    
    def __repr__(self):
        post = self
        return f"<post_id={post.id} post_title={post.title} post-content={post.content} created_at={post.created_at}>"





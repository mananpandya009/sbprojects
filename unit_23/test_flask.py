from unittest import TestCase
from app import app
from models import db, User, Post
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']



db.drop_all()
db.create_all()

class FlaskTests(TestCase):
    def setUp(self):
        """Add user"""
        User.query.delete()
        user = User(first_name="spider", last_name="man", image_url="https://tinyurl.com/28rkavzz")
        db.session.add(user)
        db.session.commit()
        post  = Post(title="post1", content="content for post1", created_at = "5pm EST 2-26-2022", user_id = user.id)
        db.session.add(post)
        db.session.commit()
        self.user_id = user.id
        self.post_id = post.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()


    def test_user_list(self):
        with app.test_client() as client:
            res = client.get('/users')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('spider', html)


    def test_add_new_user_form_view(self):
        with app.test_client() as client:
            res = client.get('/users/new')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<form action="/users/new" method="POST">', html)


    def test_edit_user_form_view(self):
        with app.test_client() as client:
            res = client.get(f'/users/{self.user_id}/edit')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(f'<form action="/users/{self.user_id}/edit" method="POST">', html)
            

    def test_user_detail(self):
        with app.test_client() as client:
            res = client.get(f'/{self.user_id}')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2 style="margin-bottom: 10px;">spider man</h2>', html)

    
    def test_post_list(self):
        with app.test_client() as client:
            res = client.get(f'/{self.user_id}')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('post1', html)
    

    def test_add_new_post_form_view(self):
        with app.test_client() as client:
            res = client.get(f'/users/{self.user_id}/posts/new')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<p style="font-size: 20px">Hello there! Please enter the post details</p><br>', html)


    def test_edit_post_form_view(self):
        with app.test_client() as client:
            res = client.get(f'/posts/{self.post_id}/edit')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(f'<form action="/posts/{self.post_id}/edit" method="POST">', html)

    
    def test_post_detail(self):
        with app.test_client() as client:
            res = client.get(f'/posts/{self.post_id}')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2>post1</h2>', html)


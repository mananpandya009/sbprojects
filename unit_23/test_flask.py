from unittest import TestCase
from app import app
from models import db, User
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
        self.user_id = user.id


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
            self.assertIn('<form action="/users/new" method="POST">', html)


    def test_edit_user_form_view(self):
        with app.test_client() as client:
            res = client.get(f'/users/{self.user_id}/edit')
            html = res.get_data(as_text=True)
            self.assertIn(f'<form action="/users/{self.user_id}/edit" method="POST">', html)
            

    def test_user_detail(self):
        with app.test_client() as client:
            res = client.get(f'/{self.user_id}')
            html = res.get_data(as_text=True)
            self.assertIn('<h2>spider man</h2>', html)

    
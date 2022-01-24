from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    def test_index(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<P>Hello there! Please enter your name to start the game!!</P><br>', html)


    def test_initiate_session(self):
        with app.test_client() as client:
            res = client.post('/init', data={'username': 'mnn'})
            print(res)
            self.assertEqual(len(session['board']), 5)
            self.assertEqual(res.status_code, 302)
            self.assertEqual(session['username'], "mnn")
            self.assertEqual(session['score'],0)
            self.assertEqual(session['guesses'],[])


    # def test_show_board(self):
    #     with app.test_client() as client:
    #         res = client.get('/board')
    #         html = res.get_data(as_text=True)

    #         self.assertEqual(res.status_code, 200)
    #         self.assertIn('<form action=""><label for="guess">Enter your guess here:</label><br>', html)

    
    # def test_process_guess(self):
    #     with app.test_client() as client:
    #         res = client.get('/boggleapi')
    #         self.assertEqual(res.status_code, 200)

    




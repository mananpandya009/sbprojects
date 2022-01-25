from unittest import TestCase
from app import app
from flask import session
from process_currency import ConvertAPIHelper


class FlaskTests(TestCase):
    def test_index(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<div id="input_form_div" class="input_form_div">', html)


    def test_validate_if_all_inputs_ok(self):
        with app.test_client() as client:
            res = client.post('/validate', data=dict(from_currency="usd", to_currency="usd", amount=10))
            html = res.get_data(as_text=True)
            self.assertIn('<p id="msg">The result is $ 10.0</p>', html)

            
    def test_validate_if_bad_inputs(self):
        with app.test_client() as client:
            res = client.post('/validate', data=dict(from_currency="sdsd", to_currency="ewe", amount=10))
            html = res.get_data(as_text=True)
            self.assertIn('<p class="error">Not a valid [FROM] currency: sdsd</p>', html)
            self.assertIn(' <p class="error">Not a valid [TO] currency: ewe</p>', html)

    
    def test_validate_if_no_inputs(self):
        with app.test_client() as client:
            res = client.post('/validate', data=dict(from_currency="", to_currency="", amount=""))
            html = res.get_data(as_text=True)
            self.assertIn('<p class="error">No data was entered!!</p>', html)

import json
import unittest

from src.api.app import app

class AppTests(unittest.TestCase):
    def setUp(self):
        self.url = "/api/predict"
        self.api = app.test_client()

    def test_does_not_categorize_product_with_empty_input(self):
        with self.api as c:
            response = c.post(self.url,
                              data=json.dumps({}),
                              content_type='application/json')
            assert response.status_code == 400

    def test_does_not_categorize_product_with_invalid_input(self):
        with self.api as c:
            given_product = json.dumps({"name": "Cama de cachorro"})
            response = c.post(self.url,
                              data=given_product,
                              content_type='application/json')
            assert response.status_code == 422

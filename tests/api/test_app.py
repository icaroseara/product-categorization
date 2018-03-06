# encoding=utf8
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

    def test_categorize_product_with_valid_input(self):
        description = u"""
        Indicada para cães adultos de raça pequena, Ração Sabor Frango,
        Contem apenas ingredientes nobres e selecionados sob rigoroso controle de qualidade,
        Pelagem bonita e saudável, rico em acido graxo essenciais, Omega 3 e Omega 6,
        Ajuda no equilibrio intestinal, combinação de ingredientes de alta digestibilidade,
        fibras alimentares e prebioticos, Enriquecido com vitaminas e minerais que proporcional
        maior saúde e vitalidade
        """
        given_product = {
            "name": u"Ração Premier Pet Formula Cães Adultos Raças Pequenas",
            "description": description
        }
        with self.api as c:
            response = c.post(self.url,
                              data=json.dumps(given_product),
                              content_type='application/json')
            assert response.status_code == 200

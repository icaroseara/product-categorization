import unittest
import pytest

from src.api.schemas.product_schema import ProductSchema

class ProductSchemaTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validate_valid_product(self):
        product = {"name": "Produt name", "description": "Some description"}
        assert ProductSchema().load(product)

    def test_validate_invalid_product(self):
        product = {"name": "Produt name"}
        validation = ProductSchema().load(product)
        assert len(validation.errors['description']) == 1

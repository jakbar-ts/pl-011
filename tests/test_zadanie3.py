from unittest import TestCase
from uuid import UUID

from src.zadanie3 import deserialize_product


class TestDeserializeProduct(TestCase):
    def test_deserialize_product_positive(self):
        # Given
        json_data = '{"id": "123e4567-e89b-12d3-a456-426614174000", "name": "Product1", "price": 10.5}'

        # When
        deserialized_product = deserialize_product(json_data)

        # Then
        self.assertIsInstance(deserialized_product, dict)
        self.assertEqual(deserialized_product['id'], UUID('123e4567-e89b-12d3-a456-426614174000'))
        self.assertEqual(deserialized_product['name'], 'Product1')
        self.assertEqual(deserialized_product['price'], 10.5)

    def test_deserialize_product_negative(self):
        invalid_json_data = '{"id": "123e4567-e89b-12d3-a456-426614174000", "name": "Product1"}'

        deserialized_product = deserialize_product(invalid_json_data)

        self.assertIsNone(deserialized_product)
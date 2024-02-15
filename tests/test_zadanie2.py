from datetime import datetime
from unittest import TestCase

from src.zadanie2 import serialize_student


class TestSerializeStudent(TestCase):
    def test_serialize_student(self):
        student_data = {
            'id': '652',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'date_of_birth': datetime(2000, 1, 1)
        }

        serialized_student = serialize_student(student_data)

        self.assertIsInstance(serialized_student, str)

        self.assertIn('"id": "652"', serialized_student)
        self.assertIn('"first_name": "John"', serialized_student)
        self.assertIn('"last_name": "Doe"', serialized_student)
        self.assertIn('"email": "john.doe@example.com"', serialized_student)
        self.assertIn('"date_of_birth": "2000-01-01"', serialized_student)
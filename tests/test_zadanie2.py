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

        self.assertEqual(serialized_student["id"], 652)
        self.assertIn(serialized_student["first_name"], "John")
        self.assertIn(serialized_student["last_name"], "Doe")
        self.assertIn(serialized_student["email"], "john.doe@example.com")
        self.assertIn(serialized_student["date_of_birth"], "2000-01-01")
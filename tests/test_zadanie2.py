from datetime import datetime
from unittest import TestCase

from src.zadanie2 import serialize_student


class TestSerializeStudent(TestCase):
    def test_serialize_student(self):
        # Given
        student_data = {
            'id': '652',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'date_of_birth': datetime(2000, 1, 1)
        }

        expected = '{"id": 652, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "date_of_birth": "2000-01-01"}'

        # When
        serialized_student = serialize_student(student_data)

        # Then
        self.assertEqual(serialized_student, expected)
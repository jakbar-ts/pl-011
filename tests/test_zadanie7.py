from unittest import TestCase

from src.zadanie7 import calculate_distance


class TestCalculateDistance(TestCase):
    def test_distance(self):
        self.assertEqual(calculate_distance(0, 0, 3, 4), 5.0)
        self.assertEqual(calculate_distance(-1, -1, 2, 3), 5.0)
        self.assertEqual(calculate_distance(1, 1, 1, 1), 0.0)
        self.assertEqual(calculate_distance(5, 5, 5, 10), 5.0)

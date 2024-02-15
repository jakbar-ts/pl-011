from unittest import TestCase
from src.zadanie1 import file_sum

class TestFileSum(TestCase):
    def test_positive_numbers(self):
        self.assertEqual(file_sum("../tests_files/test_file.txt"), 55)

    def test_negative_numbers(self):
        self.assertEqual(file_sum("../tests_files/test_file_negative.txt"), -45)

    def test_empty_file(self):
        self.assertEqual(file_sum("../tests_files/empty_file.txt"), 0)

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            file_sum("../tests_files/nonexistent_file.txt")

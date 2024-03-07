from unittest import TestCase

from src.zadanie6 import CaesarCipher


class TestCaesarCipher(TestCase):
    def test_encrypt(self):
        cipher = CaesarCipher(3)
        self.assertEqual(cipher.encrypt("abc"), "def")
        self.assertEqual(cipher.encrypt("XYZ"), "ABC")
        self.assertEqual(cipher.encrypt("Hello, World!"), "Khoor, Zruog!")

    def test_decrypt(self):
        cipher = CaesarCipher(3)
        self.assertEqual(cipher.decrypt("def"), "abc")
        self.assertEqual(cipher.decrypt("ABC"), "XYZ")
        self.assertEqual(cipher.decrypt("Khoor, Zruog!"), "Hello, World!")
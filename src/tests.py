from unittest import TestCase
from .exercises import add, substract, multiply, divide


class Tests(TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(3, 5), 8)

    def test_substract(self):
        self.assertEqual(substract(5, 3), 2)
        self.assertEqual(substract(2, 2), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(3, 9), 27)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(12, 3), 4)

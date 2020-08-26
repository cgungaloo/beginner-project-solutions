import unittest
from . import fibonacci

class TestFibonnaci(unittest.TestCase):
    expected_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_fibonacci_by_recursion(self):
        for i, expected_number in enumerate(self.expected_numbers):
            self.assertEquals(expected_number, fibonacci.find_fibonacci_by_recursion(i))

    def test_fibonacci_by_loop(self):
        for i, expected_number in enumerate(self.expected_numbers):
            self.assertEquals(expected_number, fibonacci.find_fibonacci_by_loop(i))


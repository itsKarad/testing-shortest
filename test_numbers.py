import unittest
from script import numbers

class TestNumbers(unittest.TestCase):
    def setUp(self):
        self.nums = numbers()

    def test_add(self):
        self.assertEqual(self.nums.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.nums.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.nums.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.nums.divide(6, 3), 2)

if __name__ == '__main__':
    unittest.main()
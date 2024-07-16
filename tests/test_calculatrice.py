import unittest
from src.calculatrice import addition, soustraction, multiplication, division

class TestCalculatrice(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)
        self.assertEqual(soustraction(1, 1), 0)
        self.assertEqual(soustraction(0, 5), -5)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(-1, 4), -4)
        self.assertEqual(multiplication(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(5, 2), 2.5)
        self.assertRaises(ValueError, division, 5, 0)

if __name__ == '__main__':
    unittest.main()
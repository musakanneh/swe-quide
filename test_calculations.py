#!/usr/bin/python3


"""Import the testing model
+ functions

"""
import unittest
import calculations


class TestCalculations(unittest.TestCase):
    """Testing the calculation programs"""

    def test_add(self):
        """Testing the addition of numbers"""
        self.assertEqual(calculations.add(10, 5), 15)

    def test_subtract(self):
        """Testing the subtraction of numbers"""
        self.assertEqual(calculations.subtract(500, 100), 400)

    def test_mul(self):
        """Testing the multiplication of numbers"""
        self.assertEqual(calculations.mul(10, 2), 20)

    def test_subtract(self):
        """Testing the division of numbers"""
        self.assertEqual(calculations.subtract(10, 4), 6)


if __name__ == '__main__':
    """Test control"""
    unittest.main()

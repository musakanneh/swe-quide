#!/usr/bin/python3


"""Import the testing model
+ program  for testing

"""
import unittest
import calculations


class TestCalculations(unittest.TestCase):
    """Testing the calculation programs"""

    def test_add(self):
        """Testing the addition of numbers"""
        self.assertEqual(calculations.add(10, 5), 15)
        self.assertEqual(calculations.add(100, 5), 105)
        self.assertEqual(calculations.add(20, 5), 25)

    def test_subtract(self):
        """Testing the subtraction of numbers"""
        self.assertEqual(calculations.subtract(500, 100), 400)
        self.assertEqual(calculations.subtract(500, 400), 100)

    def test_mul(self):
        """Testing the multiplication of numbers"""
        self.assertEqual(calculations.mul(10, 2), 20)
        self.assertEqual(calculations.mul(10, 0), 0)
        self.assertEqual(calculations.mul(10, 10), 100)

    def test_divide(self):
        """Testing the division of numbers"""
        self.assertEqual(calculations.divide(10, 5), 2)
        self.assertEqual(calculations.divide(50, 10), 5)
        
        # using contex manager to test for edge cases
        with self.assertRaises(ValueError):
            calculations.divide(10, 2)


if __name__ == '__main__':
    """Test control"""
    unittest.main()

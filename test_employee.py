#!/usr/bin/python3


"""Import the unittest model
+ program  for testing

"""
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """A test class for the employee's model"""

    def test_email(self):
        """Testing  email for validity"""

        first_employee = Employee("musa", "kanneh", 50000)
        second_employee = Employee("kanneh", "musa", 60000)

        self.assertEqual(first_employee.email, "musa.kanneh@email.com")
        self.assertEqual(second_employee.email, "kanneh.musa@email.com")

        """Indicating first names to the email addresses
        that are initially assigned
        
        """
        first_employee.first_name = "Tarinho"
        second_employee.first_name = "Phyta"

        self.assertEqual(first_employee.email, 'Tarinho.kanneh@email.com')
        self.assertEqual(second_employee.email, 'Phyta.musa@email.com')

    def test_full_name(self):
        """Testing for employee's full name"""

        first_employee = Employee('Musa', 'Kanneh', 50000)
        second_employee = Employee('Kanneh', 'Musa', 60000)

        self.assertEqual(first_employee.full_name, 'Musa Kanneh')
        self.assertEqual(second_employee.full_name, 'Kanneh Musa')

        """Indicating first names to the email addresses
        that are initially assigned

        """
        first_employee.first_name = "Tarinho"
        second_employee.first_name = "Phyta"

        self.assertEqual(first_employee.full_name, 'Tarinho Kanneh')
        self.assertEqual(second_employee.full_name, 'Phyta Musa')

    def test_apply_raises(self):
        """Testing for employee's payment raises"""

        first_employee = Employee('Musa', 'Kanneh', 50000)
        second_employee = Employee('Kanneh', 'Musa', 60000)

        first_employee.apply_raises()
        second_employee.apply_raises()

        self.assertEqual(first_employee.pay_bills, 52500)
        self.assertEqual(second_employee.pay_bills, 63000)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3


"""Import the unittest model
+ program  for testing

"""
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """A test class for the employee's model

    """

    @classmethod
    def setUpClass(cls):
        """Static method for set-up
        """
        print("SetUpClass")

    @classmethod
    def tearDownClass(cls):
        """Static method for tear-down

        """
        print("tearDownClass\n")

    def setUp(self):
        """Runs codes within here before every single test
        Description:
            Creates to employees before every test case
            is implemented

        """
        print("setUp")
        self.first_employee = Employee("Musa", "Kanneh", 50000)
        self.second_employee = Employee("Kanneh", "Musa", 60000)

    def tearDown(self):
        """Runs codes within here after every single test

        """
        pass

    def test_email(self):
        """Testing  email for validity

        """
        print("test_email")
        self.assertEqual(self.first_employee.email, "Musa.Kanneh@email.com")
        self.assertEqual(self.second_employee.email, "Kanneh.Musa@email.com")

        """Indicating first names to the email addresses
        that are initially assigned
        
        """
        self.first_employee.first_name = "Tarinho"
        self.second_employee.first_name = "Phyta"

        self.assertEqual(self.first_employee.email, 'Tarinho.Kanneh@email.com')
        self.assertEqual(self.second_employee.email, 'Phyta.Musa@email.com')

    def test_full_name(self):
        """Testing for employee's full name

        """
        print("test_full_name")
        self.assertEqual(self.first_employee.full_name, 'Musa Kanneh')
        self.assertEqual(self.second_employee.full_name, 'Kanneh Musa')

        """Indicating first names to the email addresses
        that are initially assigned

        """
        self.first_employee.first_name = "Tarinho"
        self.second_employee.first_name = "Phyta"

        self.assertEqual(self.first_employee.full_name, 'Tarinho Kanneh')
        self.assertEqual(self.second_employee.full_name, 'Phyta Musa')

    def test_apply_raises(self):
        """Testing for employee's payment raises

        """
        print("test_apply_raises")
        self.first_employee.apply_raises()
        self.second_employee.apply_raises()

        self.assertEqual(self.first_employee.pay_bills, 52500)
        self.assertEqual(self.second_employee.pay_bills, 63000)


if __name__ == '__main__':
    unittest.main()

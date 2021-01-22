import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """A test class for the employee's model"""

    def test_email(self):
        """Testing employee's email validity"""

        # Creates to employees
        email_1 = Employee('musa', 'kanneh', 50000)
        email_2 = Employee('kanneh', 'musa', 60000)

        # Asserts test cases
        self.assertEqual(email_1.email, 'nusakanneh@email.com')
        self.assertEqual(email_2.email, 'kannehmusa@email.com')

        """Indicating first names to the email addresses
        that are initially assigned
        
        """
        email_1.first_name = "tarinho"
        email_2.first_name = "phyta"

        self.assertEqual(email_1.email, 'tarinhokanneh@email.com')
        self.assertEqual(email_2.email, 'phytamusa@email.com')

    def test_full_nam(self):
        """Testing for employee's full name"""

        # Creates to employees
        email_1 = Employee('musa', 'kanneh', 50000)
        email_2 = Employee('kanneh', 'musa', 60000)

        # Asserts test cases
        self.assertEqual(email_1.email, 'nusakanneh@email.com')
        self.assertEqual(email_2.email, 'kannehmusa@email.com')

        """Indicating first names to the email addresses
        that are initially assigned
        
        """
        email_1.first_name = "tarinho"
        email_2.first_name = "phyta"

        self.assertEqual(email_1.email, 'tarinhokanneh@email.com')
        self.assertEqual(email_2.email, 'phytamusa@email.com')

    def test_full_name(self):
        pass


if __name__ == '__main__':
    unittest.main()

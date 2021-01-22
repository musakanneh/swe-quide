#!/usr/bin/python3

class Employee:
    """A simple employee class

    Description:
        Sets the employee's first and last name
        with methods that returns them artributes

    """
    raise_amt = 1.05

    def __init__(self, first_name, last_name, pay_bills):
        """I stantiating the employee's artributes

        Args:
            first():
            last():
            pay(int):

        """
        self.first_name = first_name
        self.last_name = first_name
        self.pay_bills = pay_bills

    def email(self):
        """Employe's email method"""
        return ("{}.{}@email.com".format(self.first, self.last))

    def full_name(self):
        """Returns the employee's full name"""
        return ("{} {}".format(self.first, self.last))

    def apply_raises(self):
        self.pay_bills = int(self.pay_bills * self.raise_amt)

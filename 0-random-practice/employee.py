#!/usr/bin/python3

class Employee:
    """A simple employee class
    Description:
        Sets the employee's first and last name
        with methods that returns them artributes
    """
    raise_amt = 1.05

    def __init__(self, first_name, last_name, pay_bills):
        """Instantiating the employee's artributes
        Args:
            first():
            last():
            pay(int):
        """
        self.first_name = first_name
        self.last_name = last_name
        self.pay_bills = pay_bills

    @property
    def email(self):
        """Employe's email method"""
        return ("{}.{}@email.com".format(self.first_name, self.last_name))

    @property
    def full_name(self):
        """Returns the employee's full name"""
        return ("{} {}".format(self.first_name, self.last_name))

    def apply_raises(self):
        self.pay_bills = int(self.pay_bills * self.raise_amt)

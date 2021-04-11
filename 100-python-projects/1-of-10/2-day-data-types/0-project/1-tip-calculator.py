#!/usr/bin/python
"""Restaurent tape calculator that:
    - Gets the total bill
    - Gets the number of people to split the bill
    - Gets the percentage of tip you would like to give?
    - The program then calculates and displays the amount each person
    is suppose to pay
"""


class TipCaculator:
    """Class mode for the calculator"""

    total_bill = input("What was total bill: ")
    total_people = input("How many people to split the bill?: ")
    bill_percent = input("What percentage tip would like to give?: ")

    def __init__(self):
        """Constructs bill payment"""
        pass

    def calculate_percentage(self):
        """Calculates the the amount a person can pay
        """
        print("Each person will: {}".format())

    def individual_amount(self):
        """Returns the amount each person will pay from the bill
        """
        if type(TipCaculator.total_bill) not in [int, float]:
            raise ValueError("bill must be in number(s)")
        return (TipCaculator.total_bill / TipCaculator.total_people)

    def tip_percent(self):
        """Returns a person's contribution to the general tip"""
        if type(TipCaculator.total_bill) not in [int, float]:
            raise ValueError("bill must be in number(s)")

        return (TipCaculator.bill_percent / 100) * (1 / TipCaculator.total_bill


if __name__ == '__main__':
    out_put=TipCaculator()

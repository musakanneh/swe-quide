#!/usr/bin/python3
"""Leap Year Indicator"""


def leap_year_indicator():
    """Works out weather a given year is a leap year
    """
    year = int(input("Which year do you want to check?: "))

    if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        print("Leap year")
    else:
        print("Not leap year")


print(leap_year_indicator())

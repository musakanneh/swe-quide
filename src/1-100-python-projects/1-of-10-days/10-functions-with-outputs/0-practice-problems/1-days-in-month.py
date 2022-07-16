#!/usr/bin/python3
"""Days in month"""


def is_leap_year(year):
    """Works out weather a given year is a leap year

    Args:
        year(int): year to in input
    """
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    return False


def days_in_month(year, month):
    """Gets a year and month and determines the num of days

    Arg:
        year(int): current year
        month(int): current month
    """
    if month > 12 or month < 1:
        return "Invalid input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month == 2:
        return 29
    return month_days[month - 1]


if __name__ == '__main__':
    """Controls functional inputs and print days"""
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)

#!/usr/bin/python3
"""Odd or Even number"""


def odd_or_even():
    """Determines number value from user input"""
    user_num = int(input("Which number do you want to check? "))

    if user_num % 2 == 0:
        print("{} is an even number".format(user_num))
    else:
        print("{} is an odd number".format(user_num))


print(odd_or_even())

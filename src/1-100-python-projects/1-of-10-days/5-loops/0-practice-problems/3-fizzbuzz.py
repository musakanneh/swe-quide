#!/usr/bin/python3
"""Fizz Buzz"""


def fizz_buzz():
    """Automatically prints the solution to  FizzBuzz game
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


print(fizz_buzz())

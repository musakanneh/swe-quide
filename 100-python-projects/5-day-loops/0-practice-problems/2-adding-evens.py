#!/usr/bin/python3
"""Adding even numbers"""


def add_even_numbers():
    """Calculates the sum of all even numbers from 1 - 100"""
    total_even_number = 0

    for number in range(1, 101):
        if number % 2 == 0:
            total_even_number += number
    print(total_even_number)


print(add_even_numbers())

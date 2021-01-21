#!/usr/bin/python3


def add(x, y):
    """Adds two numbers

     Args:
        x(int): integer input
        y(int): integer input

    """
    if not isinstance(x, int):
        raise ValueError("Number must be an integer")
    return x + y


def subtract(x, y):
    """Subtracts two numbers and validates res

    Args:
        x(int): integer input
        y(int): integer input

    Raises:
        ValueError: if resuts is too big

    """
    result = x - y
    if result >= 100:
        raise ValueError("Result is too big")
    return result


def mul(x, y):
    """Multiplies two numbers

     Args:
        x(int): integer input
        y(int): integer input

    """
    return x * y


def divide(x, y):
    """Divides to numbers

     Args:
        x(int): integer input
        y(int): integer input

    """
    if y == 0:
        raise ValueError("Can't divide by 0")
    return x / y

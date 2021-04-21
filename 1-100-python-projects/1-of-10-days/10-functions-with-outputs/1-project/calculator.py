#!/usr/bin/python3
"""Calculator App"""

from art import logo


def add(num_1, num_2):
    """Adds two numbers"""
    return num_1 + num_2


def subtract(num_1, num_2):
    """Subtracts two numbers"""
    return num_1 - num_2


def multiply(num_1, num_2):
    """Multiplies two numbers"""
    return num_1 * num_2


def divide(num_1, num_2):
    """Divides two numbers"""
    return num_1 / num_2


# A dictionary of possible operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    """Implements the calcultions"""
    num_input_1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        ops_symbols = input("Pick an operation: ")
        num_input_2 = float(input("What is the next number? "))
        calculation_function = operations[ops_symbols]
        result = calculation_function(num_input_1, num_input_2)

        print("{} {} {} = {}".format(
            num_input_1, ops_symbols, num_input_2, result))

        end_calculation = input(
            "Type y to continue calculating with {} or n to start a new calculation: ".format(result)).lower()
        if end_calculation == "y":
            num_input_1 = result
        else:
            should_continue = False
            calculator()


if __name__ == '__main__':
    calculator()

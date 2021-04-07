#!/usr/bin/python3
"""Python Pizza"""


def order_pizza():
    """Executes pizza orders"""
    print("Welcome to Python Pizza Deliveries")

    size = input("What size do you want: S, M, or L: ")
    add_pepperoni = input("Do you want pepperoni? Y or N: ")
    extra_cheese = input("Do want extra cheese? Y or N: ")
    total_bill = 0

    if size == "S":
        total_bill += 15
    elif size == "M":
        total_bill += 20
    else:
        total_bill += 25

    if add_pepperoni == "Y" and size == "S":
        total_bill += 2
    else:
        total_bill += 3

    if extra_cheese == "Y":
        total_bill += 1

    print("Your final bill is ${}".format(total_bill))


print(order_pizza())

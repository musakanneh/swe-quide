#!/usr/bin/python3
"""Rollercoaster"""


def rollercoaster():
    """Decides who to ride the roller coaster,
    with indicated height"""
    print("Welcome to the rollercoaster")
    user_height = int(input("What's your height in cm? "))
    bill = 0

    if user_height >= 120:
        print("You can ride the rollercoaster")
        user_age = int(input("What's your age? "))

        if user_age <= 12:
            bill = 5
            print("Child tickets are  $5")
        elif user_age <= 18:
            bill = 7
            print("Youth tickets are $7.")
        else:
            bill = 12
            print("Adult tickets are $12.")

        wants_photo = input("Do you want a photo taken? Y or N: ")
        if wants_photo == "Y":
            bill += 3

        print("Your final bill is ${}".format(bill))
    else:
        print("Sorry, you have to grow taller before you can ride")


print(rollercoaster())

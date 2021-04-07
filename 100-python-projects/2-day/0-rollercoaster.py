#!/usr/bin/python3
"""Rollercoaster"""


def rollercoaster():
    """Decides who to ride the roller coaster, with indicated height
    """
    print("Welcome to the rollercoaster")
    user_height = int(input("What's your height in cm? "))
    total_bill = 0

    if user_height >= 120:
        print("You can ride the rollercoaster")
        user_age = int(input("What's your age? "))

        if user_age <= 12:
            total_bill = 5
            print("Child tickets are  $5")
        elif user_age <= 18:
            total_bill = 7
            print("Youth tickets are $7.")
        elif user_age >= 45 and user_age <= 55:
            print("Everything's going to be ok. Have a free on ride on us")
        else:
            total_bill = 12
            print("Adult tickets are $12.")

        wants_photo = input("Do you want a photo taken? Y or N: ")
        if wants_photo == "Y":
            total_bill += 3

        print("Your final bill is ${}".format(total_bill))
    else:
        print("Sorry, you have to grow taller before you can ride")


print(rollercoaster())

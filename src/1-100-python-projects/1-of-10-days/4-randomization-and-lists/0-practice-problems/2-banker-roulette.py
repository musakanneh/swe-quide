#!/usr/bin/python3
"""Banker roulette - who will pay the bill"""

import random


def banker_roulette():
    """Determines the person to pay for the meal
    """
    name_string = input("Give me everybody's name, separated by a comma: ")
    if type(name_string) != str:
        raise ValueError("Name(s) must be a string")

    names = name_string.split(", ")
    names_item = len(names)
    random_choice = random.randint(0, names_item - 1)
    person_to_pay = names[random_choice]

    print("{} is going to buy the meal today".format(person_to_pay))


print(banker_roulette())

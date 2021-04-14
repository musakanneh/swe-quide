#!/usr/bin/python3
"""Virtual coin toss program: Heads or Tails"""

import random


def virtual_coin_toss():
    """ Randomly tells the user "Heads" or "Tails"
    """
    print("Welcome to the random coin generator: Heads or Tails")

    ran_coin = random.randint(0, 1)
    if ran_coin == 1:
        print("Heads")
    else:
        print("Tails")


print(virtual_coin_toss())

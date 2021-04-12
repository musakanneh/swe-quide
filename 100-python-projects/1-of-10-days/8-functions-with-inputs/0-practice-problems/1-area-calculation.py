#!/usr/bin/python3
"""Area Calculation"""

import math  # Converts decimals to int numbers


def area_calculation(height, weight, cover):
    """
    Calculates how many cans of paints
    you'll need to buy to paint a wall
    """

    res = math.ceil((height * weight) / cover)
    print("You will need {} cans of paint".format(res))


if __name__ == '__main__':
    test_h = int(input("Height of wall: "))
    test_w = int(input("Weight of wall: "))
    coverage = 5
    area_calculation(height=test_h, weight=test_w, cover=coverage)

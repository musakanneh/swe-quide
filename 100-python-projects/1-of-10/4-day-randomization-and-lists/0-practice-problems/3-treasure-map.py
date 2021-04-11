#!/usr/bin/python3
"""Treasure map"""


def treasure_map():
    """Marks a spot with an X, based on the user's choice
    """
    row_1 = ['⬜️', '⬜️', '⬜️']
    row_2 = ['⬜️', '⬜️', '⬜️']
    row_3 = ['⬜️', '⬜️', '⬜️']

    row_map = [row_1, row_2, row_3]
    print("{}\n{}\n{}".format(row_1, row_2, row_3))
    position = input("Where do you want to put the treasure?: ")

    horizontal = int(position[0])
    vertical = int(position[1])

    selected_row = row_map[vertical - 1][horizontal - 1] = " X"

    print("{}\n{}\n{}".format(row_1, row_2, row_3))


print(treasure_map())

#!/usr/bin/python3
"""Treasure Island
TODO:
    Show island upon players request
    Let a player ends the game at anytime
    Let the player go back to previous stage
"""


def treasure_island():
    """Treasure island"""
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure")
    user_direction = input(
        'You are a cross road. Where do you want to go? Type "Left" or "Right": ')
    end_game = "Game over"

    if user_direction == "Right":
        print("Fall into a whole {}".format(end_game))

    if user_direction == "Left":
        plater_decides_move = input(
            'Arrived at a lake with an island in the middle. Type "wait" to wait for a boat, or "swim" to swim across: ')

        if plater_decides_move == "wait":
            pick_color = input(
                "Arrived at the island unharmed with a house of 3 doors: Red, Yellow, and Blue. Choose a color: ")
            if pick_color == "Red":
                print("Burned by fire. {}.".format(end_game))
            elif pick_color == "Yellow":
                print("Congratulations, you win!")
            elif pick_color == "Blue":
                print("Enter by beasts. {}.".format(end_game))
            else:
                print("{}. :(".format(end_game))
        else:
            print("Eaten by a small fish. {}".format(end_game))
    else:
        print("Attacked by a trout. {}.".format(end_game))


if __name__ == '__main__':
    treasure_island()

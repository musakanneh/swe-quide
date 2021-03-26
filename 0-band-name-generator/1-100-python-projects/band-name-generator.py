#!/usr/bin/python3
"""
Gets the name of user's city and pet
Then. generates the user's band name
"""


class BandNameGenerator:
    """Model for band name generator"""

    def welcome_note(self):
        """Displays a welcome note"""
        content = [
            "Welcome to the Band Name Generator",
            "Please respond to the following questions to complet the game.",
            "Enjoy the game :)"
        ]
        for items in content:
            print(items)
    print(welcome_note(""))

    location = input("Name of the city that you grew up in: ")
    pet_name = input("Name of a pet: ")

    def __init__(self):
        """Constructs the user's location"""
        return

    def out_put(self):
        """Prints the user's band name"""
        result = BandNameGenerator.location + " " + BandNameGenerator.pet_name
        if len(BandNameGenerator.location) <= 1:
            raise TypeError("Location name too short")
        print("Your band name could be {}".format(result))


if __name__ == '__main__':
    result = BandNameGenerator()
    result.out_put()

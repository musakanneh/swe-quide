#!/usr/bin/python3
"""
Gets the name of user's city and pet
Then. generates the user's band name
"""


class BandNameGenerator:
    """Model for band name generator
    """

    def get_user_input(self):
        """Gets user's city
        """
        print("Location: ")
        user_location = input()
        if type(user_location) != str:
            raise TypeError("Location must be a string")
        return user_location

    def get_pet_name(self):
        """Gets the pet's name
        """
        print("Pet's name")
        pet_name = input()
        if type(pet_name) != str:
            raise TypeError("Location must be a string")
        return pet_name


class ProgramResult(BandNameGenerator):

    def __init__(self):
        """Constructs the user's location
    """

    def out_put(self):
        print("Output comes here")
        # return self.get_user_input()


if __name__ == '__main__':
    location = BandNameGenerator()
    pet_name = BandNameGenerator()
    location.get_user_input()
    location.get_pet_name()

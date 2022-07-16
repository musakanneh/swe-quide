#!/usr/bin/python3

age = 30
name = input("What is your name? ")


def age_is_true():
    if age <= 20:
        print("Musa Kanneh is {} years old".format(age))
    else:
        age_is_false()
        display_success_message()


def display_success_message():
    print("Information well received! Congratulations, {}!".format(name))


def age_is_false():
    if age != 20:
        print("Note Quite")
    location = ""
    get_location = input("What is your location: ")
    location += get_location
    print("This is your location {}".format(location))


def control_center():
    print("Welcome to the age calculator")
    age_is_true()


if __name__ == '__main__':
    control_center()

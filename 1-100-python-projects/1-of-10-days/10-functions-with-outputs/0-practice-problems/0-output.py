#!/usr/bin/python3
"""Format name"""


def format_name(f_name, l_name):
    """Returns the formatted names"""
    if f_name == "" or l_name == "":
        return "Invalid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return "{} {}".format(formatted_f_name, formatted_l_name)


if __name__ == '__main__':
    print(format_name(input("What is your first name? "),
                      input("What is your first name? ")))

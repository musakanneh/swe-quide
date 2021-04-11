#!/usr/bin/python3
"""Greetings"""


def greet():
    """Displays greetings"""
    print("Hello")
    print("World")
    print("It's the weather nice today?")


# greet("")


def greet_with_name(name):
    """Greetings with given name via params
    """
    print("Hello {}".format(name))
    print("How are you doing today, {}?".format(name))
    print("It's the weather nice today, {}?".format(name))


name = "John"
greet_with_name(name)

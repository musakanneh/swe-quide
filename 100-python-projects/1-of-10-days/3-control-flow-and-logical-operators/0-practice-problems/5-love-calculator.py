#!/usr/bin/python3
"""Tests the compatibility between two people
Takes both people's name and checks for the number of time
the letters in the word TRUE occurs. Then checks for the number
of time the letters in the word LOVE occurs. The combines these
numbers to make a digit number."""


def love_calculator():
    """Love score calc"""
    print("Welcome to the love calculator\n-------------------")
    name_one = input("What is your name?: ").lower()
    name_two = input("What is their name?: ").lower()
    true_value = "TRUE".lower()
    love_value = "LOVE".lower()
    love_score = 0

    for i in range(len(name_one)):
        for l in true_value:
            if name_one[i] == l:
                love_score += 1
    for j in range(len(name_two)):
        for l in love_value:
            if name_two[j] == l:
                love_score += 1

    if love_score < 10 or love_score > 90:
        print("Your score is {}, you go together like coke and mentos."
              .format(love_score))
    if love_score >= 40 and love_score <= 50:
        print("Your score is {}, you are alright together."
              .format(love_score))
    else:
        print("Your score is {}".format(love_score))
    return love_score


# print(love_calculator())


def love_calculator_ii():
    print('''
                        ________    _ _ _ _  _ ____ ___
    ______|/             | | | |__| |__|  |
    /  __       _/ _====\ |_|_| |  | |  |  |
    /  _____    /_ ____  \  ____ ____ ____    _   _ ____ _  _
    | / ____ \   /  0   \   |__| |__/ |___     \_/  |  | |  |
    \\/  0   |  \______/   |  | |  \ |___      |   |__| |__|
    |\___ . |  -- .--     _    ____ ____ _  _ _ _  _ ____
        - .  (   )  _____\  |    |  | |  | |_/  | |\ | | __
    |      ; ___/    | \ |___ |__| |__| | \_ | | \| |__]
        \    __/ _ | _|  /\ ____ ___ __.
        | /(_|_| |____/    |__|  |   _|
        \   ____          |  |  |   .
        ''')
    print("Welcome to the love calculator")
    name_1 = input("What is your name?: ")
    name_2 = input("What is their name?: ")

    combined_string = name_1 + name_2
    lower_case_string = combined_string.lower()

    t = lower_case_string.count("t")
    r = lower_case_string.count("r")
    u = lower_case_string.count("u")
    e = lower_case_string.count("e")

    true = t + r + u + e

    l = lower_case_string.count("l")
    o = lower_case_string.count("o")
    v = lower_case_string.count("v")
    e = lower_case_string.count("e")

    love = l + o + v + e

    love_score = int(str(true) + str(love))

    if love_score < 10 or love_score > 90:
        print("Your love score is  {}, you go together like coke and mentos".format(
            love_score))
    elif love_score >= 40 and love_score <= 50:
        print("Your score is  {}, you alright together".format(love_score))
    else:
        print("Your score is {}")
    print(love_score)


print(love_calculator_ii())

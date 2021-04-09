#!/usr/bin/python3
"""Highest score"""


def highest_score():
    """
    Gets a list of students score and outputs
    the highest score in the class
    """
    student_scores = input("Input a list of students scores: ").split()
    for i in range(len(student_scores)):
        student_scores[i] = int(student_scores[i])

    current_highest_score = 0
    for score in student_scores:
        if score > current_highest_score:
            current_highest_score = score
    print("The highest score in the class is: {}".format(current_highest_score))


print(highest_score())

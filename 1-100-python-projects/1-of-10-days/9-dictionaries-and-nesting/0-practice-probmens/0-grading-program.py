#!/usr/bin/python3
"""Grading program"""


def grading_program():
    """Converts students score to grades, with description"""
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62
    }

    student_grades = {}

    for student in student_scores:
        score = student_scores[student]
        if score > 90:
            student_grades[student] = "Outstanding"
        elif score > 80:
            student_grades[student] = "Exceeds expectations"
        elif score > 70:
            student_grades[student] = "Exceptable"
        else:
            student_grades[student] = "Fail"

    print(student_grades)


if __name__ == '__main__':
    grading_program()

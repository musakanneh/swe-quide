#!/usr/bin/python3
"""Average student heigh"""


def average_height():
    """Gets lists of students heights and return the avg
    """
    students_height = input("Input a list of students height: ").split()
    for i in range(0, len(students_height)):
        students_height[i] = int(students_height[i])

    total_height = num_of_students = 0

    for height in students_height:
        total_height += height
    for student in students_height:
        num_of_students += 1

    average_height = round(total_height / num_of_students)
    print("Average height is {}".format(average_height))


print(average_height())

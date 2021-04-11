#!/usr/bin/python3
"""Calculating BMI"""


def bmi_calculator():
    """Interprets the body mass index (BMI)
    on a user weight and height"""
    user_height = float(input("Enter your height in meter: "))
    user_weight = float(input("Enter your weight in kg: "))
    bmi = round(user_weight / user_height ** 2)

    if type(user_weight) not in [float]:
        raise ValueError("Weight must be a decimal number")

    if bmi < 18.5:
        print("Your bmi is {}, and you are underweight".format(bmi))
    elif bmi < 25:
        print("Your bmi is {}, and you have a normal weight".format(bmi))
    elif bmi < 30:
        print("Your bmi is {}, and you are overwright".format(bmi))
    elif bmi < 35:
        print("Your bmi is {}, and you are obese".format(bmi))
    else:
        print("Your bmi is {}, and you are clinically obese".format(bmi))


print(bmi_calculator())

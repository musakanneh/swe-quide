#!/usr/bin/python3
"""Prime Number Checker"""


def check_prime(number):
    """Gets a number and tells weather it's a prime or not"""
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's is prime number")
    else:
        print("It's not a prime number")


if __name__ == '__main__':
    n = int(input("Check this number: "))
    check_prime(number=n)

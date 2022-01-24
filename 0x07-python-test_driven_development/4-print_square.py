#!/usr/bin/python3

"""
    Task 4 - Mandatory
"""


def print_square(size):
    """
        Method - prints in stdout the square with the character #.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        else:
            print()

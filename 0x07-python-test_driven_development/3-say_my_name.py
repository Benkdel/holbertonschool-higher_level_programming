#!/usr/bin/python3
"""
    Task 3 - Mandatory
"""


import string


def say_my_name(first_name, last_name=""):
    """
        Prints my name is fn ln
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if (last_name == ""):
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))

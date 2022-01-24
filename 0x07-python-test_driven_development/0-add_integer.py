#!/usr/bin/python3
"""
    First mandatory task
"""


def add_integer(a, b=98):
    """
        function that adds 2 integers
        float is valid only if it can be cast to an integer
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)

#!/usr/bin/python3
"""
    Functions:
        a) lookup
"""


def lookup(obj):
    """
        Functions - List of available attributes and methods of an object:
        Args:
            obj (object): Any instance
        Return:
            The list of available attributes and methods of an object
    """
    return dir(obj)

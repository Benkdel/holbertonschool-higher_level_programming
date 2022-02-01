#!/usr/bin/python3
"""
    Task 8 - Mandatory
"""


def class_to_json(obj):
    """
        Returns:
            dictionary description of an object
    """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res

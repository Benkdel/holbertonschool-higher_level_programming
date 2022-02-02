#!/usr/bin/python3
"""
    Task 6 - Mandatory
"""

import json


def load_from_json_file(filename):
    """
        Creates an Object from JSON file
    """
    with open(filename, mode="r", encoding="utf-8") as dest_file:
        return (json.load(dest_file))

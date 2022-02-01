#!/usr/bin/python3
"""
    Task 5 - Mandatory
"""

import json


def save_to_json_file(my_obj, filename):
    """
        Writes an Object to a textfile
                    using JSON rep
    """
    with open(filename, mode="w", encoding="utf-8") as dest_file:
        json.dump(my_obj, dest_file)

    dest_file.close()

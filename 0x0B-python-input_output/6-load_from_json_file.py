#!/usr/bin/python3
"""
    Task 6 - Mandatory
"""

import json


def load_from_json_file(filename):
    """
        Creattes an Object from JSON file
    """
    with open(filename, mode="w", encoding="utf-8") as dest_file:
        json.loads(dest_file)
    
    dest_file.close()

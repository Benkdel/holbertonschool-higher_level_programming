#!/usr/bin/python3
"""
    Task 4 - mandatory
"""

import json


def from_json_string(my_str):
    """
        Returns:
            object represented by a JSON string
    """
    return (json.loads(my_str))

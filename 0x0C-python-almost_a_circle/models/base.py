#!/urs/bin/python3
"""
    Base Class
"""

import json


class Base:
    """
        Base Class
        Handles IDs for all children
    """
    __nb__objects = 0

    def __init__(self, id=None):
        """
            Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns:
                JSON string of list_dic...
        """
        if list_dictionaries is None or list_dictionaries[0] == None:
            return ("[]")

        return (json.dumps(list_dictionaries))

    
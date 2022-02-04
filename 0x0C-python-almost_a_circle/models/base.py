#!/urs/bin/python3
"""
    Module to define Base Class
"""


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

#!/usr/bin/python3
"""
    Square
"""

from rectangle import Rectangle


class Square(Rectangle):
    """
        Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Constructor
                handled by super class
        """
        super().__init__(size, size, x, y, id)

    " ================ Python Builtint Methods ================ "

    def __str__(self):
        """
            Override str method
        """
        description = "[Square] ({}) <{}/{}> - <{}>".format(
            self.id, self.x, self.y, self.width)
        return (description)

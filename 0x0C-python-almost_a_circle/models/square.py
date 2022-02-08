#!/usr/bin/python3
"""
    Class Square
"""

from models.rectangle import Rectangle


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

    " ================ Getters ================ "

    @property
    def size(self):
        """
            Size Getter
        """
        return (self.width)

    " ================ Setters ================ "

    @size.setter
    def size(self, value):
        """
            Size Setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    " ================ Public Methods ================ "

    def update(self, *args, **kwargs):
        """ Method: Update the Square,
            that assigns an argument to each attribute,
            in the order (id, size, x, y)
            Args:
                args (list): A list of new values to atributes.
                kwargs (dict): A dictionary of new values to atributes.
        """
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                self.id = (args[i] if i == 0 else self.id)
                self.size = (args[i] if i == 1 else self.size)
                self.x = (args[i] if i == 2 else self.x)
                self.y = (args[i] if i == 3 else self.y)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Dictionary representation
        """
        key_list = ["id", "size", "x", "y"]
        value_list = [self.id, self.size, self.x, self.y]
        return dict(zip(key_list, value_list))

    " ================ Python Builtint Methods ================ "

    def __str__(self):
        """ Method (custom): Get format string for the Square.
            Returns:
                The representation in str for the Square.
                -'[Square] (<id>) <x>/<y> - <size>'-
            """
        str_squa = "({}) ".format(self.id)
        str_squa += "{}/{} - ".format(self.x, self.y)
        str_squa += "{}".format(self.size)
        return ("[Square] " + str_squa)

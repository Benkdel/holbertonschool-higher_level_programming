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
        """
            Assigns attributes
            **kwargs skipped if *args is passed
        """
        arg_list = ["id", "size", "x", "y"]
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, arg_list[i], args[i])
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

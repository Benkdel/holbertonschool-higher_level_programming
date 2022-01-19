#!/usr/bin/python3

"""Class documentation"""


class Square:
    """Class documentation"""

    def __init__(self, size=0):
        """__init__ constructor method"""
        self.__size = size

    @property
    def size(self):
        """Size Property Getter"""
        return self.__size
    
    @size.setter
    def size(self, size):
        """Size Property Setter"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method to calculate area of instansiated square"""
        return self.__size * self.__size

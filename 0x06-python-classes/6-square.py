#!/usr/bin/python3

class Square():

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size
    
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2:
            for item in value:
                if type(item) is int and item >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.__size == 0):
            print("\n")
        else:
            for rows in range(0, self.__size):
                for cols in range(0, self.__size):
                    print("#", end="")
                print(end="\n")

#!/usr/bin/python3
"""
    Class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
        Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Constructor
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    " ================ Getters ================ "

    @property
    def width(self):
        """
            Width Getter
        """
        return (self.__width)

    @property
    def height(self):
        """
            Height Getter
        """
        return (self.__height)

    @property
    def x(self):
        """
            x Getter
        """
        return (self.__x)

    @property
    def y(self):
        """
            y Getter
        """
        return (self.__y)

    " ================ Setters ================ "

    @width.setter
    def width(self, value):
        """
            Width Setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
            Height Setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """
            x Setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """
            y Setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    " ================ Public Methods ================ "

    def area(self):
        """
            Returns:
                Area of the Rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
            Prints Rectangle Instance
            using "#"
        """
        print("\n"*self.__y, end="")
        for row in range(0, self.__height):
            print(" "*self.__x, end="")
            for col in range(0, self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
            Assigns attributes
            **kwargs skipped if *args is passed
        """
        args_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, args_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Dictionary representation
        """
        key_list = ["id", "width", "height", "x", "y"]
        value_list = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(key_list, value_list))

    " ================ Python Builtint Methods ================ "

    def __str__(self):
        """
            Override str method
        """
        description = "[Rectangle] ({}) <{}/{}> - <{}/{}>".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return (description)

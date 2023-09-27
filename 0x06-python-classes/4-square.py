#!/usr/bin/python3
"class square"


class square:
    "representation"

    def __init__(self, size=0):
        "instantiation"
        self.size = size

    @property
    def size(self):
        "property to retrieve the value of size"
        return self.size

    @size.setter
    def size(self, value):
        """Property setter to set size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        "public instance methode that return area of square"
        return self.__size ** 2

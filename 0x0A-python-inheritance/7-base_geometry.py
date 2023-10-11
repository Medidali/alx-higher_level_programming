#!/usr/bin/python3
"ClassGeometrie"


class BaseGeometry:
    """class geometrie"""

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation that value is a positif integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise valueError("{:s} must be greater than 0".format(name))

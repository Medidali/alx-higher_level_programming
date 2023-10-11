#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""

    def __init__(self, width, height):
        """initialisation"""
        self._width_ = width
        self._height_ = height

    from 7-base_geometry import integer_validator
    integer_validator(name, value)
    

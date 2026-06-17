#!/usr/bin/python3
"""Module that defines a square."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        # Assigning to self.size here automatically calls the setter method!
        self.size = size

    @property
    def size(self):
        
        return self.__size

    @size.setter
    def size(self, value):
        
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value

    def area(self):
        
        return self.__size ** 2

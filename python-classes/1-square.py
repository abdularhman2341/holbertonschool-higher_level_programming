#!/usr/bin/python3
"""Module that defines a square."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize the square with a given size.

        Args:
            size: The size of the square (no type/value verification yet).
        """
        self.__size = size

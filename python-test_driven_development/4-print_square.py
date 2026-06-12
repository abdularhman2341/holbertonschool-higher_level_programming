#!/usr/bin/python3
"""
Module to print a square using the character #.
"""

def print_square(size):
    """Prints a square with the character # of a given size."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
        
    for i in range(size):
        print("#" * size)

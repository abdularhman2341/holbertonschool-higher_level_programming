#!/usr/bin/python3
"""
Module for addition of two integers.
"""

def add_integer(a, b=98):
    """Adds two integers after checking their types and casting floats to ints."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

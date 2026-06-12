#!/usr/bin/python3
"""
Module to divide all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number."""
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
        
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"
    
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(msg_type)
        
    row_length = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg_type)
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError(msg_size)
            
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(msg_type)
                
    return [[round(item / div, 2) for item in row] for row in matrix]

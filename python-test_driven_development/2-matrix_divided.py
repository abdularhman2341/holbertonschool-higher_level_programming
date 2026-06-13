#!/usr/bin/python3
"""
Module to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number."""
    if type(div) not in [int, float] or div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(msg)

    r_len = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)
        if r_len is None:
            r_len = len(row)
        elif len(row) != r_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(msg)

    return [[round(i / div, 2) for i in row] for row in matrix]

#!/usr/bin/python3
"""
Definning a function which divises a matrix.
"""



def matrix_divided(matrix, div):
    """Divides all the elements of a matrix.
    Arguments:
    Raises:
    Returns:
    """
    if isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("")

    if div == 0:
        raise ZeroDivisionError("")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

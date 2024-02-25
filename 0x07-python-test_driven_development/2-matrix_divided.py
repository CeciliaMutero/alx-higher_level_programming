#!/usr/bin/python3
"""
Define function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Parameters:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The divisor to divide each element of the matrix.

    Returns:
    list of lists: A new matrix with each element divided by the divisor.

    Raises:
    TypeError: If the matrix is not a list of lists.
    TypeError: if the divisor is not an int or float.
    ZeroDivisionError: If the divisor is zero.
    TypeError: If each row of the matrix does not have the same size.
    """
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(num / div, 2) for num in row] for row in matrix]

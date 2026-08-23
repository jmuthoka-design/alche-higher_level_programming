#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix

    Args:
        matrix: a 2 dimensional list of integers

    Returns:
        A new matrix of the same size, with each value squared.
        The original matrix is not modified.
    """
    return [[value ** 2 for value in row] for row in matrix]

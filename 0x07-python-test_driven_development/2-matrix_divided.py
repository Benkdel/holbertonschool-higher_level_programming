#!/usr/bin/python3

"""
    Task 2 - Task 1 is missing from the intranet
"""


def matrix_divided(matrix, div):
    """
        Function to divide every element 
        of a matrix by a number
    """
    err_message_1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_message_2 = "Each row of the matrix must have the same size"
    err_message_3 = "div must be a number"
    err_message_4 = "division by zero"
    row_size = -1
    new_matrix = []

    if type(matrix) is not list:
        raise TypeError(err_message_1)
    else:
        for row in matrix:
            if type(row) is not list:
                raise TypeError(err_message_1)
            else:
                if row_size > -1 and row_size != len(row):
                    raise TypeError(err_message_2)
                row_size = len(row)
                for item in row:
                    if type(item) not in [int, float]:
                        raise TypeError(err_message_1)
    if type(div) not in [int, float]:
        raise TypeError(err_message_3)
    if div == 0:
        raise ZeroDivisionError(err_message_4)

    for row in matrix:
        tmp = []
        for item in row:
            tmp.append(round(item / div, 2))
        new_matrix.append(tmp)
    return new_matrix

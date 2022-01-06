#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[(matrix[x][y]**2) for y in range(3)] for x in range(3)]
    return new_matrix

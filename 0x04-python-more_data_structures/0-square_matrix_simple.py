#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        square_matrix.append([(num * num) for num in row])
    return (square_matrix)

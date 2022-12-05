#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return (matrix)
    for row in range(len(matrix)):
        for num in range(len(matrix[row])):
            if num == len(matrix[row]) - 1:
                print("{:d}".format(matrix[row][num]), end="")
            else:
                print("{:d}".format(matrix[row][num]), end=" ")
        print("{}".format(""))

# Class to solve a system of equations using the Gaussian method.
import os
import sys


class SystemEquations(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.leading_variables = []

    def find_leading_variables(self):
        variables = []
        for i in range(len(self.matrix)):
            row = self.matrix[i]
            for j in range(len(row)):
                cell = row[j]
                if cell != 0:
                    variables.append((cell, i, j))
                    break
        self.leading_variables = variables

    def is_in_echelon_form(self):
        positions = []
        self.find_leading_variables()
        for variable in self.leading_variables:
            value, row_index, col_index = variable
            if value != 1:
                return False
            positions.append(col_index)
        for i in range(len(positions) - 1):
            if positions[i] >= positions[i+1]:
                return False
        return True

    def is_in_row_reduced_echelon_form(self):
        if not self.is_in_echelon_form():
            return False
        for variable in self.leading_variables:
            value, row_index, col_index = variable
            column = [row[col_index] for row in self.matrix if row[col_index] != value]
            for cell in column:
                if cell != 0:
                    return False
        return True


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 1],
        [0, 1, 0, -1],
        [0, 0, 1, 3],
        [0, 0, 0, 0]
    ]
    new_system = SystemEquations(matrix)
    print(new_system.is_in_echelon_form())
    print(new_system.is_in_row_reduced_echelon_form())

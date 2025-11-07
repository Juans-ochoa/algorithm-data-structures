from typing import Any

from arrays.array import Array2D


class Matrix[T: (int, float, complex)]:
    def __init__(self, rows: int, cols: int) -> None:
        self._the_grid = Array2D[T](rows, cols)
        self._the_grid.clear(0)

    # Returns the number of rows in the matrix
    def num_rows(self) -> int:
        return self._the_grid.num_rows()

    # Returns the number of columns in the matrix
    def num_cols(self) -> int:
        return self._the_grid.num_cols()

    # Returns the value of element (i,j):x[i,j]
    def __getitem__(self, ndx_tuple: tuple[int, int]):
        return self._the_grid[ndx_tuple[0], ndx_tuple[1]]

    # Sets the value of element (i,j):x[i,j]
    def __setitem__(self, ndx_tuple: tuple[int, int], scalar: Any):
        self._the_grid[ndx_tuple[0], ndx_tuple[1]] = scalar

    # Scale the matrix by the scalar
    def scale_by(self, scalar: int | float):
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                self[i, j] *= scalar

    # Transpose
    def transpose(self):
        pass

    # Create and returns a new matrix that is the result of adding this matrix to ghe rsh_matrix, both matrix sizes is the same.
    def add(self, rsh_matrix: "Matrix[T]") -> "Matrix[T]":
        assert rsh_matrix.num_rows() == self.num_rows() and  \
            rsh_matrix.num_cols() == self.num_cols(), \
            "Matrix sizes not compatible for the add operation"

        # Create the new matrix
        new_matrix = Matrix[T](self.num_rows(), self.num_cols())

        # Add corresponding elements in the two matrices
        for r in range(self.num_rows()):
            for c in range(self.num_cols()):
                new_matrix[r, c] = self[r, c] + rsh_matrix[r, c]

        return new_matrix

    # Subtract the same as the add() operations but subtracts the two matrix
    def subtract(self, rsh_matrix: Any): pass

    # Multiply - Creates and return a new matrix that is the result of multiplying this matrix to geh given rsh_matrix
    def multiply(self, rsh_matrix: Any): pass

from arrays.array import Array

TNdxTuple = tuple[int, int]


class _MatrixElementNode:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None


class SparseMatrix:
    def __init__(self, num_rows: int, num_cols: int):
        self._num_cols = num_cols
        self._list_rows = Array(num_rows)

    # Returns the number of tows int the matrix
    def num_rows(self):
        return len(self._list_rows)

    # Return the number of columns in the matrix
    def num_cols(self):
        return self._num_cols

    # Return the value of element (i,j):x[i,j]
    def __getitem__(self, ndx_tuple: TNdxTuple):
        pass

    # Set the value of element(i,j) th the value s: x[i,j] = s
    def __setitem__(self, ndx_tuple: TNdxTuple, value):
        row, col = ndx_tuple

        prev_node = None
        cur_node = self._list_rows[row]

        while cur_node is not None and cur_node.col != col:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is not None and cur_node.col == col:
            if value == 0.0:  # Remove the node
                if cur_node == self._list_rows[row]:
                    self._list_rows[row] = cur_node.next
                else:
                    prev_node.next = cur_node.next
            else:
                cur_node.value = value
        # Otherwise, the element is not in the list
        elif value != 0.0:
            new_node = _MatrixElementNode(col, value)
            new_node.next = cur_node

            if cur_node == self._list_rows[row]:
                self._list_rows[row] = new_node
            else:
                prev_node.next = new_node

    # Scales the matrix by the given scalar
    def scale_by(self, scalar):
        for row in range(self.num_rows()):
            cur_node = self._list_rows[row]

            while cur_node is not None:
                cur_node.value *= scalar
                cur_node = cur_node.next

    # Creates and returns a new Matrix that is the transpose of this matrix
    def transpose(self):
        pass

    # Matrix addition: newMatrix = self + rhsMatrix
    def __add__(self, rhs_matrix):
        assert rhs_matrix.num_rows() == self.num_rows() and \
            rhs_matrix.num_cols() == self.num_cols(), \
            "Matrix sizes not compatible for adding"

        # Create a new matrix to the new matrix
        new_matrix = SparseMatrix(
            num_rows=self.num_rows(), num_cols=self.num_cols())

        # Add the elements of this matrix to the new matrix
        for row in range(self.num_rows()):
            cur_node = rhs_matrix._list_rows[row]

            while cur_node is not None:
                new_matrix[row, cur_node.col] = cur_node.value
                cur_node = cur_node.next

        # Add the elements of the rhs_matrix to the new Matrix
        for row in range(rhs_matrix.num_rows()):
            cur_node = rhs_matrix._list_rows[row]
            while cur_node is not None:
                value = new_matrix[row, cur_node.col]
                value += cur_node.value
                new_matrix[row, cur_node.col] = value
                cur_node = cur_node.next

        return new_matrix

    # Matrix subtraction
    def __sub__(self, rhs_matrix):
        pass

    # Matrix multiplication
    def __mul__(self, rhs_matrix):
        pass

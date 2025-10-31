import ctypes
from typing import Any, Self


class _ArrayIterator[T]:
    def __init__(self, array: "Array[T]") -> None:
        self._array_ref = array
        self._cur_index = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry

        raise StopIteration


class Array[T]:
    def __init__(self, size: int) -> None:
        assert size > 0, "Array size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object * self._size
        self._elements = PyArrayType()
        self.clear(None)  # pyright: ignore[reportUnknownMemberType]

    # Return the size of the array
    def __len__(self) -> int:
        return self._size

    # Gets the contents of the index element
    def __getitem__(self, index: int) -> T:
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    # Puts the value in the array element at index position.
    def __setitem__(self, index: int, value: T):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value

    # Clears the array by setting each element to the given value.
    def clear(self, value: None | str | int | float | T | Any) -> None:
        for i in range(len(self)):
            self._elements[i] = value

    # Return the array's iterator for traversing the elements
    def __iter__(self):
        return _ArrayIterator[T](self)


# ArrayType = ctypes.py_object * 5
# slots = ArrayType()

# for i in range(5):
#     slots[i] = None

# slots[0] = 10
# slots[2] = 20
# slots[4] = 30

# for i in range(5):
#     print(slots[i])


class Array2D[T]:
    # Create a 2-D array of size num_rows X num_cols
    def __init__(self, rows: int, cols: int) -> None:
        # Create a 1-D array to store an array reference for each row.
        self._rows: Array[Array[T]] = Array(rows)

        # Create the 1-D array for each row of the 2-D array
        for i in range(rows):
            self._rows[i] = Array(cols)

    # Returns the number of rows in the 2-D array
    def num_rows(self) -> int:
        return len(self._rows)

    # Returns the number of columns in the 2-D array
    def num_cols(self) -> int:
        return len(self._rows[0])

    # Clears the array by setting every element to the given value.
    def clear(self, value: Any) -> None:
        rows: int = len(self._rows)

        for row in range(rows):
            self._rows[row].clear(value)

    # Gets the contents of the element at position[i,j]
    def __getitem__(self, ndx_tuple: tuple[int, int]) -> T:
        assert len(ndx_tuple) == 2, "Invalid number of array subscripts."
        row = ndx_tuple[0]
        col = ndx_tuple[1]

        assert row >= 0 and row < self.num_rows() \
            and col >= 0 and col < self.num_cols(), \
            "Invalid number of array subscripts."

        one_d_array = self._rows[row]
        return one_d_array[col]

    # Sets the contents of the element at position [i,j] to value.
    def __setitem__(self, ndx_tuple: tuple[int, int], value: Any):
        assert len(ndx_tuple) == 2, "Invalid number of array subscripts."
        row = ndx_tuple[0]
        col = ndx_tuple[1]

        assert row >= 0 and row < self.num_rows() \
            and col >= 0 and col < self.num_cols(), \
            "Array subscript out of range."

        the_1d_array = self._rows[row]
        the_1d_array[col] = value

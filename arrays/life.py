from arrays.array import Array2D


class LifeGrid:
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, rows: int, cols: int) -> None:
        self._grid: "Array2D[int]" = Array2D(rows, cols)

        # Clear the grid and set all cells to dead.
        self.configure(list())

    # Returns the number of rows in the grid.
    def num_rows(self) -> int:
        return self._grid.num_rows()

    # Return the number of columns in the grid.
    def num_cols(self) -> int:
        return self._grid.num_cols()

    # Configure grid
    def configure(self, coord_list: list[tuple[int, int]]):
        # Clear the game grid.
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                self.clear_cell(i, j)

        # Set the indicated cells to be alive.
        for coord in coord_list:
            self.set_cell(coord[0], coord[1])

    # Does the indicated cell contain a live organism?
    def is_live_cell(self, row: int, col: int) -> bool:
        return self._grid[row, col] == self.LIVE_CELL

    # Clears the indicated cell by setting it go dead.
    def clear_cell(self, row: int, col: int) -> None:
        self._grid[row, col] = self.DEAD_CELL

    # Sets the indicated cell to be alive.
    def set_cell(self, row: int, col: int) -> None:
        self._grid[row, col] = self.LIVE_CELL

    # Returns the number fo live neighbors for given cell.
    def num_live_neighbors(self, row: int, col: int):
        pass

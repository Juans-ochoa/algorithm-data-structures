from life import LifeGrid

# Define the initial configuration of live cells.
INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]

# Set the size of the grid.
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of generations.
NUM_GENS = 8


def main():
    # Construct the game grid and configure it.
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # Play the game.
    # draw(grid)
    for _ in range(NUM_GENS):
        evolve(grid)
        draw(grid)


def evolve(grid: "LifeGrid"):
    # Generate the next generation of organisms.
    live_cells: list[tuple[int, int]] = list()

    # Iterate over the elements of the grid.
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):
            # Determine the number of live neighbors for this cell.
            neighbors = grid.num_live_neighbors(i, j)

            # Add the (i,j) tuple to live_cells if this cell contains a live organism in the next generation.
            if (neighbors == 2 and grid.is_live_cell(i, j)) or \
                    (neighbors == 3):
                live_cells.append((i, j))

    # Reconfigure the grid using the live_cells coord list.
    grid.configure(live_cells)


def draw(grid: "LifeGrid"):
    # Print a text-based representation of the game grid.
    pass

#Problem: Conway gameoflife (3kyu)

"""
Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:

Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any live cell with two or three live neighbours lives on to the next generation.
Any dead cell with exactly three live neighbours becomes a live cell.
Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)

For illustration purposes, 0 and 1 will be represented as and blocks respectively (PHP, C: plain black and white squares). You can take advantage of the htmlize function to get a text representation of the universe, e.g.:

print htmlize(cells)
trace (htmlize cells)
PUZZLESGAMESARRAYS
"""


# def get_generation(cells, generations):
#     return cells


def get_generation(cells, n):



    # Stop if n is equal to 0
    if n == 0:

        # Checking if all the cells are not all alive and returning a boolean
        all_alive = any(any(state) for state in cells)

        # Checking if all the cells are not all alive.
        if not all_alive: return [[]]

        return cells

    sum_neighbors = 0
    next_state = 0
    next_gen = []

    for i in range(len(cells)):
        # A tempory empty list
        temp_list = []
        for j in range(len(cells[i])):

            """ Counting the number of living cells around each cells """
            # Top
            if i - 1 >= 0:
                sum_neighbors += cells[i - 1][j + 0]

            # Bottom
            if i + 1 < len(cells):
                sum_neighbors += cells[i + 1][j + 0]

            # Left
            if j - 1 >= 0:
                sum_neighbors += cells[i + 0][j - 1]

            # Right
            if j + 1 < len(cells[i]):
                sum_neighbors += cells[i + 0][j + 1]

            # Top Left
            if i - 1 >= 0 and j - 1 >= 0:
                sum_neighbors += cells[i - 1][j - 1]

            # Top Right
            if i - 1 >= 0 and j + 1 < len(cells[i]):
                sum_neighbors += cells[i - 1][j + 1]

            # Bottom Left
            if i + 1 < len(cells) and j - 1 >= 0:
                sum_neighbors += cells[i + 1][j - 1]

            # Bottom Right
            if i + 1 < len(cells) and j + 1 < len(cells[i]):
                sum_neighbors += cells[i + 1][j + 1]



            """ Applying the rules of the Conway Game Of Life """

            # If cell is alive

            if cells[i][j] == 1:

                # Underpopulation
                if sum_neighbors < 2:

                    next_state = 0 # Dead

                # Overcrowding
                elif sum_neighbors > 3:

                    next_state = 0 # Dead

                # Stasis
                else:

                    next_state = 1 # Stays the same 1

            else:
                # Reproduction
                if sum_neighbors == 3:

                    next_state = 1 # Live

                else:

                    next_state = 0 # Stays the smae 0



            # Updating the temp_list
            temp_list.append(next_state)

            # Reset sum_neighbors
            sum_neighbors = 0


        # Updating cells_neighbors
        next_gen.append(temp_list)

    return get_generation(next_gen, n - 1)



# Second Approach


def get_generation2(cells, n):

    if n == 0: return cells

    cells_duplica = cells

    while n > 0:

        # Checking if all the cells are not all alive and returning a boolean
        all_alive = any(any(state) for state in cells_duplica)

        # Checking if all the cells_duplica are not all alive.
        if not all_alive: return [[]]


        sum_neighbors = 0
        next_state = 0
        next_gen = []

        for i in range(len(cells_duplica)):
            # A tempory empty list
            temp_list = []
            for j in range(len(cells_duplica[i])):
                """ Counting the number of living cells around each cells_duplica """
                # Top
                if i - 1 >= 0:
                    sum_neighbors += cells_duplica[i - 1][j + 0]

                # Bottom
                if i + 1 < len(cells_duplica):
                    sum_neighbors += cells_duplica[i + 1][j + 0]

                # Left
                if j - 1 >= 0:
                    sum_neighbors += cells_duplica[i + 0][j - 1]

                # Right
                if j + 1 < len(cells_duplica[i]):
                    sum_neighbors += cells_duplica[i + 0][j + 1]

                # Top Left
                if i - 1 >= 0 and j - 1 >= 0:
                    sum_neighbors += cells_duplica[i - 1][j - 1]

                # Top Right
                if i - 1 >= 0 and j + 1 < len(cells_duplica[i]):
                    sum_neighbors += cells_duplica[i - 1][j + 1]

                # Bottom Left
                if i + 1 < len(cells_duplica) and j - 1 >= 0:
                    sum_neighbors += cells_duplica[i + 1][j - 1]

                # Bottom Right
                if i + 1 < len(cells_duplica) and j + 1 < len(cells_duplica[i]):
                    sum_neighbors += cells_duplica[i + 1][j + 1]
                """ Applying the rules of the Conway Game Of Life """

                # If cell is alive

                if cells_duplica[i][j] == 1:

                    # Underpopulation
                    if sum_neighbors < 2:

                        next_state = 0  # Dead

                    # Overcrowding
                    elif sum_neighbors > 3:

                        next_state = 0  # Dead

                    # Stasis
                    else:

                        next_state = 1  # Stays the same 1

                else:
                    # Reproduction
                    if sum_neighbors == 3:

                        next_state = 1  # Live

                    else:

                        next_state = 0  # Stays the smae 0

                # Updating the temp_list
                temp_list.append(next_state)

                # Reset sum_neighbors
                sum_neighbors = 0

            # Updating next_gen
            next_gen.append(temp_list)

        # Updating cells_duplica witht he next generation 
        cells_duplica = next_gen

        n -= 1

    return next_gen
#Test Zone

grid = [[1, 0, 1],
        [0, 1, 0],
        [1, 0, 0]]

# grid = [[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]]
print(get_generation2(grid, 0))
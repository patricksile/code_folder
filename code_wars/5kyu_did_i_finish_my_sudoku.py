### Problem: Did I Finish My Sudoku?
"""
Write a function done_or_not passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'
Sudoku Rules: : http://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com/
"""

### My Solution:
import numpy as np



board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

board2 = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]
# Solving the rows and columns checking in Sudoku of 9 * 9

def done_or_not(board): #board[i][j]
    boardnp = np.array(board) # This makes python list becomes a numpy array
    expected_axe_sum = np.array([45,45,45,45,45,45,45,45,45]) # Expected sum in any axis directions of a 9*9 Sudoku
    axe_0_sum = np.sum(boardnp, axis = 0) # Sum of axe 0 (vertical or j) in numpy array type
    axe_1_sum = np.sum(boardnp, axis = 1) # Sum of axe 1 (horizontal or i) in numpy array type

    # This is the np.all() method to check if everything in arrays validates to True
    if np.all(axe_0_sum == expected_axe_sum) and np.all(axe_0_sum == expected_axe_sum):
        boxes=[boardnp[:3,:3],boardnp[:3,3:6],boardnp[:3,6:9],boardnp[3:6,:3],boardnp[3:6,3:6],boardnp[3:6,6:9],boardnp[6:9,:3],boardnp[6:9,3:6],boardnp[6:9,6:9]]  # Boxes all in a list
        counter = 0 # Counter to initiate the count through the 9 boxes check
        for x in boxes:
            expected_box_sum = 45 # Expected sum of the items of a box
            if sum(x.reshape(-1)) == expected_box_sum: # reshape(-1) flatterns the box in a 1D (module numpy) array
                counter += 1
                if counter == 9:
                    return "Finished!"
            else:
                return "Try again!"
    else:
        return "Try again!"




print(done_or_not(board))


# Other Solutions:

# Solution 1:

import numpy as np
def done_or_not(aboard): #board[i][j]
  board = np.array(aboard)
  # List comprehension to collect rows in an array and columns(cols) in an array also
  rows = [board[i,:] for i in range(9)]
  cols = [board[:,j] for j in range(9)]
  # List comprehension to collect boxes(sqrs) on th board and flatterning them at one
  # The use of 2 for here to generate the coordinate of rows and columns in each boxes
  # flatten() is used here to flatten the collect coordinates into a 1D array.
  sqrs = [board[i:i+3,j:j+3].flatten() for i in [0,3,6] for j in [0,3,6]]
  # vstack() is used to put all the ndarrays in 1D, and unique() returns the unique elements
  # of an array all sorted, like set.
  for view in np.vstack((rows,cols,sqrs)):
      if len(np.unique(view)) != 9:
          return 'Try again!'

  return 'Finished!'











assert done_or_not( [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])  == 'Finished!'

assert done_or_not( [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]])  == 'Try again!'

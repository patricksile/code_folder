# Problem: Directions Reduction (5kyu)
"""
... a man was given directions to go from one point to another. The directions were
"NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST"
and "EAST" too. Going to one direction is a needless effort. Since this is a wild
west, with dreadfull weather and not much water, it's important to save yourself
some energy, otherwise you might die of thirst!
How I crossed the desert the smart way.
The directions given to the man are, for example, the following:
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
or
{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"}

The good answer is WEST since there is not need to go Nord the South which is
actually like going nowhere.

Task:

Write a function dirReduc which will take an array of strings and returns an array
of strings with the needless directions removed(w <-> E or S <-> N side by side).
"""

# My Solution:


def dirReduc(arr):

    # Test cases
    test_arr = [("NORTH", "SOUTH"), ("SOUTH", "NORTH"), ("EAST", "WEST"), ("WEST", "EAST")]

    # First obvious conditions
    # if arr == None or arr == [None] or arr == 'None' or arr == ["None"]:
    #     return []
    # elif arr == []:
    #     return []
    # elif tuple(arr) in test_arr:
    #     return []
    # elif len(arr) == 1:
    #     return arr
    counter = 0  # Counter

    # While loop for other conditions
    while counter < len(arr) - 1:
        if (arr[counter], arr[counter + 1]) in test_arr:
            arr.remove(arr[counter + 1])
            arr.remove(arr[counter])
            counter = 0
            if arr == []:
                return []
            elif counter + 1 == len(arr):
                return arr
        elif counter + 1 == len(arr) - 1:
            return arr
        else:
            counter += 1


dir_arr = ["NORTH", "EAST"]
# dir_arr = ["EAST"]
# dir_arr = None
# dir_arr = [None]
# dir_arr = 'None'
# dir_arr = ["None"]
# dir_arr = []
# dir_arr = ["NORTH", "WEST", "SOUTH", "EAST"]
# dir_arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

print dirReduc(dir_arr)

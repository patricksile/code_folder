# Problem: Snail (4kyu)

"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]

"""
# My Solution:

# sq = [[1,2,3,4,88],
#       [5,6,7,8,88],
#       [9,10,11,12,88],
#       [13,14,15,16,88],
#       [17,18,19,20,88]]
# sq = [[1,2,3,4],
#       [5,6,7,100],
#       [9,10,11,12],
#       [13,14,15,16]]
sq = [[1,2,3],
      [5,6,7],
      [9,10,11]]
def snail(array):
    p_x_axis = []
    n_x_axis = []
    p_y_axis = []
    n_y_axis = []
    snail_track = []
    l = len(array)
    counter = 0
    while counter < l / 2 :
        print(counter)
        p_x_axis = array.pop(0)
        snail_track += p_x_axis
        if array != []:
            n_x_axis = array.pop(-1)[::-1]
        else:
            break
        for point in array: 
            p_y_axis.append(point.pop(-1))
            n_y_axis.insert(0, point.pop(0))
        snail_track += p_y_axis + n_x_axis + n_y_axis
        p_y_axis.clear()
        n_y_axis.clear()


        counter += 1
    return snail_track

print(snail(sq))

[3].count
# Other Solutions:

# Solution 1: By foxxyz, JasonFTW, Aweson2, polarizing, __TomFoolery__, shikha2017 (plus 4 more warriors)

def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []


# Solution 2: By MMMAAANNN, ruoyuchen, Alexkington, guest_elkfct_i0qk
def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = zip(*array)
        array.reverse()
    return a

# Solution 3: By Speedy

# my implementation/explanation of the solution by foxxyz
def snail(array):
  if array:
    # force to list because zip returns a list of tuples
    top_row = list(array[0])
    # rotate the array by switching remaining rows & columns with zip
    # the * expands the remaining rows so they can be matched by column
    rotated_array = zip(*array[1:])
    # then reverse rows to make the formerly last column the next top row
    rotated_array = rotated_array[::-1]
    return top_row + snail(rotated_array)
  else:
    return []

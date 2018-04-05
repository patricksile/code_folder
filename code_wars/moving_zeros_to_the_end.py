### Problem: Moving Zeros To The End (5kyu)
"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the oder elements.

Example:

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""
### My Solutions:

def move_zeros(array):
    zero, non_zero = [],[]
    for value in array:
        if value == 0 and value is not False:
            zero.append(0)
        else:
            non_zero.append(value)
    return non_zero + zero

# Other Solutions:

# Solution 1: By riyakayal

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

# Solution 2: By bevoy, percy22, Pixie11

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

array = [1,{},1,0,False,0,3,0,None,[],1,0,2,"a",0,0]
# array = [9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]
# array = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
# array = [0, 9, 9, 1, 2, 0, 1, 0, 1, 3, 1, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]

print move_zeros(array)

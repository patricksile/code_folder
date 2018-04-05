# Problem: N_centered (beta 5kyu)
"""
An array is called centered-N if some consecutive sequence of elements of the array sum to N and this sequence is preceded and followed by the same number of elements.

Example:

[3,2,10,4,1,6,9] is centered-15
because the sequence 10,4,1 sums to 15 and the sequence
is preceded by two elements [3,2] and followed by two elements [6,9]
write a method called isCenteredN that returns true if its array argument is not empty and centered-N but the inner array might be empty and that sum will be 0,otherwise it returns false.

"""
# My Solution:


def is_centered(arr,n):
    if len(arr) < 1: return False
    counter = 0
    while counter <= len(arr) // 2:
        if sum(arr[counter : len(arr) - counter]) == n:return True
        counter += 1
    return False
# Other Solutions:
# Solution 1: By kjmosher

def is_centered(arr,n):
    return n in (sum(arr[i:-i or None]) for i, __ in enumerate(arr)) or not n

# Solution 2: By akshaykalyan

def is_centered(arr,n):
    t=[]
    for x in range((len(arr)//2)+1):
        t.append(sum(arr[x:(len(arr)-x)]))
    return n in t


# [3,2,10,4,1,6,9] is centered-15

print(is_centered([], 0))

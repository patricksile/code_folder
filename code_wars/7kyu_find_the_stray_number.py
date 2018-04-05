#!/usr/bin/env python3.5
# Problem: Find the stray number (7kyu)
"""
You are given an odd-length array of integers, in which all of them are the same
, except for one single number.
Implement the method stray which accepts such array, and returns that single
different number.

The input array will always be valid!(odd-length >= 3)

Examples:
[1,1,2] => 2
[17,17,3,17,17,17,17,17] =>3
"""
# My solution:

def stray(arr):
    for i in range(len(arr) -1):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            return arr[i]
    return arr[len(arr)-1]

# Other Solutions:

# Solution 1: By cvillian098, snormandeau, Mr.Child, rlqmal
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x

# Solution 2: By EDjur, george166
# This is the more clever solution.
def stray(arr):
    # key is a function so min will return the minimum count value
    return min(arr, key=arr.count)




lst = [3,345,3,3]

print(stray(lst))

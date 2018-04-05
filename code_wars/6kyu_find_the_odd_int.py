#!/usr/bin/env python3.5
# Problem: Find the odd into (6kyu)

"""
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Example:

find_it([20,1,-1,-2,2,3,3,5,5,1,2,4,20,4,-1,-2,5]) => 5

"""

# My Solution:

def find_it(seq):

    # Tuple of Set.
    tuple_set = tuple(set(seq))
    # Count occurences
    for i in tuple_set:
        if seq.count(i) % 2 != 0:
            return i

# One line version with a generator comprehension

def find_it(seq):
    return next(i for i in seq if seq.count(i) % 2 != 0)

# Other Solutions:

# Solution 1: By Dupa, Mr.Child

def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]

print(find_it([20,1,-1,2,-2,3,3,3,5,5,1,2,4,20,4,-1,-2,5,5]))

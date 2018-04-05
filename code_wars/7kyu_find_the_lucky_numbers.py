#!/usr/bin/env python3.5
# Problem: Find the lucky numbers(7kyu)
"""
Write a function filter_lucky() that accepts a list of integers and filters the
list to only include the elements that contain the digit 7.
Example:
filter_lucky([1,2,3,4,5,7,68,69,70,15,17]) => [7,70,17]
"""
# My Solution:

def filter_lucky(lst):
    return[lst[i] for i in range(len(lst)) if '7' in str(lst[i])]

# Other Solutions:
# Solution 1:
def filter_lucky(lst):
    return [ n for n in lst if '7' in str(n) ]
l = [1,2,3,4,5,7,68,69,70,15,17]
print(filter_lucky(l))

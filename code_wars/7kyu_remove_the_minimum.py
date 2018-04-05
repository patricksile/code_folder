#!/usr/bin/env python3.5
# Problem: Remove the minimum (7kyu)

"""
The Museum of incredible dull things
The museum of incredible dull things wants to get rid of some exhibitions. Miriam. The interior architect, comes up with a plan to remove the most
boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

TASK

Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the value, remove the one with a lower index. If you get an empty array/list. Return an empty
array/list.

Don't change the order of the elements that are left.

EXAMPLES:

remove_smallest([1,2,3,4,5]) = [2,3,4,5]
remove_smallest([5,3,2,1,4]) = [5,3,2,4]
remove_smallest([2,2,1,2,1]) = [2,2,2,1]
"""
# My Solution:

def remove_smallest(numbers):
    if numbers == []:
        return []
    numbers.remove(min(numbers))
    return numbers

# Other Solutions:

# Solution 1: By Emigre, Syim, JustyFy

def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers

# Solution 2: By itay3x3

def remove_smallest(numbers):
    return[numbers[i] for i in range(len(numbers)) if i != numbers.index(min(numbers))]

print(remove_smallest([1,2,1,3,4]))

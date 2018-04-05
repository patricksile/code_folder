#!/usr/bin/env python3.5
import random
# Problem: Enough is enough! (6kyu)


"""
Alice and Bob were on a holiday. Both of them took many pictures of the places
they've been, and now they want to show Charlie their entire collection. However,
Charlie doesn't like this sessions, since the motive usually repeats. He isn't
fond of seeing the Eiffel tower 40 times. He tells them that he will only sit
during the session if they show the same motive at most N times.
Luckily, Alice and Bob are able to encode the motive as a number. Can you help
them to remove numbers such that their list contains each number only up to N
times, without changing the order?

TASK:

Given a list lst and a number N, create a new list that contains each number of
lst at most N times without reordering.

Examples:
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you only keep [1,2,3,1,2,3]

delete_nth([1,1,1,1], 2) # returns [1,1]
delete_nth(([20,37,20,21], 1)) # returns [20,37,21]
"""

# My Solution:


# This is for the test cases
lst = [1, 3, 2, 4, 2, 1, 6, 7, 2, 1, 3, 4, 4, 4, 2, 1, 1]
# list with 20 random numbers between 1 and 6 (6 not included)
random_list = [random.randrange(1, 4) for _ in range(0, 15)]
print (random_list)


def delete_nth(order, n_occurence):
    """
    This function returns a max of n occurence(s) in
    any given list(order here)
    """
    # Initial empty list
    new_order = []

    for i in order:
        # Checking the occurence by count() in the new list
        if new_order.count(i) < n_occurence:
            new_order.append(i)
    return(new_order)


print (delete_nth(random_list, 2))

# Other Solutions:

# Solution 1:
#
from collections import Counter


def delete_nth(order, max_e):
    c = Counter()
    result = []
    for element in order:
        if c[element] < max_e:
            c[element] += 1
            result.append(element)
    return result

# Solution 2:


def delete_nth(order, max_e):
    """
    You add an element in the output only if there is lesser occurencies of the same element than max_e before current index.
    So as long as you haven't encouter max_e occurencies, they are added to the output.
    Once you have found max_e occurencies, they are rejected
    # Explained by "lechevalier"
    """
    return [order[i] for i in range(len(order)) if order[0:i + 1].count(order[i]) <= max_e]

# def delete_nth2(o, n):
#     new_o = []
#     return [new_o.append(i) for i in o if new_o.count(i) < n]


# print(delete_nth2(random_list, 2))

# Problem: Unique in order(6kyu)
"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""
# My Solution:

def unique_in_order(it):
    return [j for i, j in enumerate(it) if j != it[i - 1] or i == 0] if it else []

# Other Solutions:

# Solution 1: By kmeshu09, 文刀七禾页, skpolina

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

# Solution 2: By natict, Unnamed, chanshik, banebot, NishthaMishra

from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

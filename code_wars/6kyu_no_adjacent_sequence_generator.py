# Problem: No Adjacent Sequence Generator (6kyu)
"""

"""
# My Solution:


def generate_sequence(lower, upper):
    return list(range(lower + 1, upper, 2)) + list(range(lower, upper, 2))

# Other Solutions:

# Solution 1: By siebenschlaefer, Blind4Basics

def generate_sequence(lower, upper):
    return list(range(lower+1, upper, 2)) + list(range(lower, upper, 2))

# Solution 2: By Unnamed, simosini

from itertools import chain

def generate_sequence(lower, upper):
    return list(chain(range(lower + 1, upper, 2), range(lower, upper, 2)))

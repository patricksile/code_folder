#!/usr/bin/env python3.5
# Problem: Find the GCF of Two Numbers (7kyu)
"""
Your task here is to find the GCF(Greatest Common Factor) of any two numbers passed
into a method, which will return one integer answer as an output.

Example:
find_GCF(4,6) => 2
find_GCF(93, 186) => 93
find_GCF(20, 5) => 5

Here, inputs will always be natural numbers so there's no need worry about negative values or zero.
"""
# My Solution:

from fractions import gcd
def find_GCF(a, b):
    return gcd(a, b)

# Other Solution:

# Solution 1: By amone, ErmesFranch

def find_GCF(a,b):
    while b:
        a, b = b, a%b
    return a

# Solution 2: By danman1979

def find_GCF(a,b):
    if b == 0: return a
    return find_GCF(b, a%b)

print(find_GCF(100080000, 1600000000000))



# Problem: Find the missing term in an Arithmetic Progression
"""
An Arithmetic Progression is defined as one in which there is a constant difference
between the consecutive terms of a given series of numbers. You are provided with
consecutive elements of na AP.
There is however one hitch: Exactly one term from the original series is missing
from the set of numbers which have been given to you. The rest of the given series
is the same as the original AP. Find the missing term.

You have to write the function find_missing(list), list will always be atleast 3
numbers. The missing term will never be the first of the last one.

Example:
`find_missing([1,3,5,9,11]) == 7`

PS: This is a sample question of the facebook engeneer challange on interviewstreet. I found it quite fun to solve on paper using math , derive the algo that way. Have fun!
"""

# My Solution:

def find_missing(seq):
	return int(0.5 * (seq[0] + seq[-1]) * (len(seq) + 1) - sum(seq))

print (find_missing([4, 9, 19, 24, 29]))

# Other Solutions:

# Solution 1: By MMMAAANNN

def find_missing(sequence):
    interval = (sequence[-1] - sequence[0])/len(sequence)
    for previous, item in enumerate(sequence[1:]):
        if item - sequence[previous] != interval:
            return item - interval

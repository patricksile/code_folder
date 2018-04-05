#!/usr/bin/env python3.5
# Problem: Counting Duplicates(6kyu)
"""
Count the number of Duplicates

Write a function that will return the count of distinct "case-insensitive" characters and numeric digits that occurs more than once in the input string. The input string can be assumed to contain only alphabets(both uppercase and lowercase) and numeric digits.

Examples:

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

"""

# Problem: Counting Duplicates (6kyu)

# My Solution:

def duplicate_count(text):
    counter = 0
    for i in set(text.upper()):
        if text.upper().count(i) > 1:
            counter += 1
    return counter
    
    
#
def duplicate_count(text):
    # Using a generator here could have used sum() or len()
    return sum( 1  for i in set(text.upper()) if text.upper().count(i) > 1)

# Exploiting the idea of lambda notation
duplicate_count = lambda text: sum( 1  for i in set(text.upper()) if text.upper().count(i) > 1)



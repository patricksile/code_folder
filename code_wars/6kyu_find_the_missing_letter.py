#!/usr/bin/env python3.5
# Problem: Find the missing letter (6kyu)

"""
# Find the missing letter

Write a method that takes an array of consecutive(increasing) letters as
input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Examples:

['a','b','c','d','f'] => 'e'
['O','Q','R','S'] => 'P'

(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)
"""
# My Solution:

from string import ascii_letters as al
def find_missing_letter(chars):
    # Valid letters, v_letters
    v_letters = al[al.index(chars[0]):(al.index(chars[-1])+1)]
    return [i for i in v_letters if i not in chars][0]

# My solution with ord() and chr():
def find_missing_letter(chars):
    for n in range(ord(chars[0]),ord(chars[-1])+1):
        if n not in [ord(c) for c in chars]:
            return chr(n)
print(find_missing_letter(['O','Q','R','S']))

# Other Solutions:

# Solution 1: By Blind4Basics
def find_missing_letter(chars):
    """
    ord(c)
    Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97

    chr(i)
    Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a',
    """
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

# Problem: Detect the pangram (6kyu)
"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
# My Solution:


def is_pangram(s):
    return  len([l for l in set(s.lower()) if l.isalpha()]) == 26

p = "The quick, brown fox jumps over the lazy dog!"
# Other Solutions:
# Solution 1: By hiasen

import string

def is_pangram(s):
    # string.lowercase works in py2, in py3 string.ascii_lowercase
    return set(string.lowercase) <= set(s.lower())

# Solution 2: By aoris, pgrzesik

import string

def is_pangram(s):
    s = s.lower()
    # string.lowercase works in py2, in py3 string.ascii_lowercase
    return all(letter in s for letter in string.lowercase)

# Problem: Contamination #1 -String
"""
An AI has infected a text with a character!!

This text is now fully mutated to this character.

If the text or the character are empty, return an empty string.
There never will be a case when both are empty as nothing is going on!!

The character is a string. It will always be of length 1 if it's not empty.

Example:

before = "abc"
character = "z"
after = "zzz"
"""

# My Solution:

def contamination(t, c):
    return "" if t == "" or c == "" else c * len(t)

def contamination(t, c):
    return len(t) * c

# Other Solutions:

# Solution 1: by Acaccia, Tachyonlabs
def contamination(text, char):
    return char * len(text)

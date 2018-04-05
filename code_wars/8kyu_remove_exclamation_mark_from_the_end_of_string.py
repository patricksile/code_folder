#!/usr/bin/env python3.5
# Problem: Exclamation marks series #1:(8kyu)
"""
Description:

Remove a Exclamation mark from the end of string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.

Examples:

remove("Hi!") => "Hi"
remove("Hi!!!") => "Hi!!"
remove("!Hi") => "!Hi"
remove("!Hi!") => "!Hi"
remove("Hi! Hi!") => "Hi! Hi"
remove("Hi") => "Hi"

"""
# My Solution:

def remove(s):
    if s and s[-1] is '!': return s[0:len(s)-1]
    return s

# Rewrite of my solution:

def remove(s):
    return s[:-1] if s and s[-1] is '!' else s
    # return s[:-1] if s and s[-1] is '!' else s

print(remove(""))

# Other Solutions:

# Solution 1: By MiraliN, aevista,Chris_Rands
def remove(s):
    return s[:-1] if s.endswith('!') else s
print(remove(""))

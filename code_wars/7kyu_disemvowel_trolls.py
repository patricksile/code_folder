#!/usr/bin/env python3.5
# Problem: Disemvowel Trolls (7kyu)
"""
Trolls are attactking your comment section!

A common way to deal with this situation is to remove all of the vowels from
the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string
with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""
# My Solution:

def disemvowel(string):
    newstring = ""
    for i in string:
        if i not in ("aeiuoyAEIUOY"):
            newstring += i
    return newstring

def disemvowel(string):
    return "".join(i for i in string if i not in ("aeiuoAEIUO"))


# Other Solutions:
# Solution 1: By cvk77, zyrolasting

# For python 2

# def disemvowel(s):
#     return s.translate(None, "aeiouAEIOU")

# For python 3
def disemvowel(s):
    translator = str.maketrans({key: None for key in "aeiouAEIOU"})
    return s.translate(translator)

def disemvowel(s):
    return s.translate(str.maketrans('','','aeiouAEIOU'))

# Solution 3: By horejsek, beastmean, Jstjames
# uses regex to do it with the sub() and a flags re.IGNORECASE
import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

print(disemvowel("This website is for losers LOL!"))

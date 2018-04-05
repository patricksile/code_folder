# Problem:
"""
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

a being 1, b being 2, etc.

As an example:

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.
"""
# My Solution:

def alphabet_position(text):
    a = 'abcdefghijklmnopqrstuvwxyz'
    return " ".join(str(a.index(l) + 1) for l in text.lower() if l.isalpha())

# Other Solutions:
# Solution 1: By laoris, murpium, CrazyMerlyn, datagram, Karan@CodeDoor

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


# Solution 2: By joeylmaalouf

def alphabet_position(s):
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())

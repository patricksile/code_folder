#!/usr/bin/env python2

# Problem: Rot13 (5kyu)

"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot 13. if there are numbers or special characaters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like the original ROT13 "implementation".
Please note that using "encode" in Python is considered cheating.
"""
## My Solution:

import string
from codecs import encode as _dont_use_this_

def rot13(message):
    pass
    low = string.lowercase  # Lowercase alphabet
    up = string.uppercase   # Uppercase alphabet
    rot13_message = ""
    for character in message:
        # Check if character is alphabetique
        if character.isalpha():
            if character in low: # Check if it is in string.lowercase
                [low.index(character) + 13]
                rot13_message += (2*low)[low.index(character) + 13]
            else:   # It is uppercase then
                rot13_message += (2*up)[up.index(character) + 13]
        else:
            rot13_message += character
    return rot13_message

message = "Testsssss"




## Other Solutions:

# Solution 1:

import string

def rot13(message):
    return message.encode("rot13")
    #oh snap
print (rot13(message))

# Solution 2:

import string
from codecs import encode as _dont_use_this_
from string import maketrans, lowercase, uppercase

def rot13(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)

#!/usr/bin/env python3.5
# Problem: Valid Braces (4kyu)
"""
Write a function called validBraces that takes a string of braces, and
determines if the order of the braces is valid, validBraces should return
true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces four
new characters. Open and closed brackets, and open and closed curly braces.

All input strings will be nonempty, and will only consist of open Parentheses
'(', closed parentheses')', open brackets '[', closed brackets ']', open Curly
braces '{' and closed curly '}'.

What is considered Valid? A string of braces is considered valid if all braces are mathed with the correct brace.

For Example:

'(){}[]' and ([{}]) would be considered valid, while '(}', '[(])', and '[({})(]' would be considered invalid.

Examples:

validBraces( "(){}[]" ) => returns true
validBraces( "(}" ) => returns false
validBraces( "[(])" ) => returns false
validBraces( "([{}])" ) => returns true

"""
import re

def validBraces(string):
    regex = re.compile(r"^(?:\[[^\[\]]*\]|{[^{}]*}|\([^\(\)]*\))+$")
    mo = regex.search(string)
    if string == None:
        return True
    elif mo:
        return True
    else:
        return False

print(validBraces("([}{])"))

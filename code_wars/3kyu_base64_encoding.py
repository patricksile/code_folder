# Problem:Base64 Encoding (3kyu)
"""
Base64 Encoding

Instructions
Output
Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.

Do not use built in functions.

Usage:

# should return 'dGhpcyBpcyBhIHN0cmluZyEh'
to_base_64('this is a string!!')

# should return 'this is a string!!'
from_base_64('dGhpcyBpcyBhIHN0cmluZyEh')
You can learn more about Base64 encoding and decoding here.
ALGORITHMSBINARYPROTOTYPESSTRINGS
"""
# My Solution:
import re
import base64
def to_base_64(string):
    return base64.standard_b64encode(string)
    
def from_base_64(string):
    return base64.standard_b64decode(string)

# Test.describe("Basic tests")
# tests = [["this is a string!!","dGhpcyBpcyBhIHN0cmluZyEh"],
#   ["this is a test!","dGhpcyBpcyBhIHRlc3Qh"],
#   ["now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
#   ["1234567890  ", "MTIzNDU2Nzg5MCAg"],
#   ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
#   ["the quick brown fox jumps over the white fence. ","dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
#   ["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4","ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
#   ["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
#   ["TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"]]

# for test in tests:
#   result = to_base_64(test[0])
#   Test.assert_equals(result, test[1])
#   Test.assert_equals(from_base_64(result), test[0])
  
# Other Solutions:

# Solution: By warriors
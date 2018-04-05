# Problem: Valid Phone Number(6kyu)

"""
Write a function that accepts a string, and returns true if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)

Examples:

validPhoneNumber("(123) 456-7890")  =>  returns true
validPhoneNumber("(1111)555 2345")  => returns false
validPhoneNumber("(098) 123 4567")  => returns false

"""
# My Solution:
import re
def validPhoneNumber(phoneNumber):
    return True if re.match(r"^\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4}$", phoneNumber) else False


# Other Solutions:
# Solution 1: By Anayat, Silver-core and More...
def validPhoneNumber(phoneNumber):
    import re
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))

# Solution 2: By HEXecutive
import re
prog = re.compile('^\(\d{3}\) \d{3}-\d{4}$')
def validPhoneNumber(phone_number):
    return prog.match(phone_number) is not None

# Solution 3: By MMMAAANNN 
validPhoneNumber = lambda x: bool(__import__('re').match('\(\d{3}\) \d{3}-\d{4}$', x))

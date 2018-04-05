#Problem: Regexp Basics - Is it a digit?

"""
Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.
"""
import re
def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def is_digit(n):
    return True if re.match(r'^[0-9]$', n) and len(n) == 1 else False

print(is_digit("1\n"))

# Other Solutions:

# Solution 1: by Faldang, TheBMachine and More ... 

def is_digit(n):
    return n.isdigit() and len(n)==1

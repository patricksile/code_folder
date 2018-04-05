#Problem:Regex Validate pin code (7kyu)
"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False

"""
# My solution:

import re
def validate_pin(pin):
    return True if re.match(r"^\d{4}$|^\d{6}$", pin) else False


# Other Solutions:

# Solution 1: By
import re
def validate_pin(pin):
    return bool(re.match(r'^(\d{4}|\d{6})$',pin))

# Solution 2: By Lechevalier, aytrack, bugaevc, andriis (plus 50 more warriors)

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

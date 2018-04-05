# Problem: IPv4 Validator (7kyu)
"""
In this kata you have to write a method to verify the validity of IPv4 addresses.

Example of valid inputs:

"1.1.1.1"

"127.0.0.1"

"255.255.255.255"

Example of invalid input:

"1444.23.9"

"153.500.234.444"

"-12.344.43.11"

"""
import re

def ipValidator(ip):
    return True if re.match(r"^([0-9]{1,3}\.){3}[0-7]{1,3}$", ip) else False

i = "255.0.0.0"
print(ipValidator(i))

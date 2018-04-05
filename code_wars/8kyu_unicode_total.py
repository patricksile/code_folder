# Problem: Unicode Total (8kyu)
"""
You'll be given a string, and have to return the total of all the unicode characters as an int. Should be able to handle any characters sent at it.

examples:

uniTotal("a") == 97 uniTotal("aaa") == 291
"""
# My Solution:

def uni_total(string):
    return sum(ord(i) for i in string)

print(uni_total("aa"))

# Other Solutions:

# Solution 1: By banksh, sebduf and more...

def uni_total(string):
    return sum(map(ord,string))

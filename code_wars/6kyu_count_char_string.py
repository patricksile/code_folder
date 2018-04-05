# Problem:
"""
The main idea is to count all the occuring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }

For C#: Use a Dictionary<char, int> for this kata!

"""
# My Solution:

def count(string):
    return {k:v for k,v in ((char,string.count(char)) for char in set(string))}
print(count("aba"))
# Other Solutions:
# Solution 1: By ChristianECooper, kevin.du, Slx64, benw413

from collections import Counter

def count(string):
    return Counter(string)

# Solution 2: By zebulan, Unnamed, daddepledge, acaccia, MFreidank, kjmosher

from collections import Counter as count

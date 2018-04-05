# Problem:
"""

"""
# My Solution:

def solution(s):
    if len(s) % 2: s += '_'
    return [s[i:i+2] for i in range(0,len(s), 2)]

# Other Solutions:
# Solution 1: By

def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

# Solution 2: anter69

import re

def solution(s):
    return re.findall(".{2}", s + "_")

# Solution 3: Weemän, tachyonlabs

def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

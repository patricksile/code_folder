# Problem:String Revisal (6kyu)
"""
In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example:

dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].
dup(["kelless","keenness"]) = ["keles","kenes"].
Strings will be lowercase characters only. See test cases for more examples.

Good luck!
"""
# My Solution:
def dup(arr):
    
    res = []
    
    for word in arr:

        word = list(word)
        
        for i in range(len(word) - 1):
    
            if word[i] == word[i+1]:

                word[i] = ''

        res.append(''.join(word))

    return res


   # return [word[i] for word in arr for i in range(len(word) - 1) if word[i] != word[i+1]]



test1 = ["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]
print(dup(test1))
# Other Solutions:

# Solution: By warriors mentalplex

from itertools import groupby

def dup(arry):
    return ["".join(c for c, grouper in groupby(i)) for i in arry]


# Solution: By warriors Unnamed

from itertools import groupby

def dup(strings):
    return [''.join(c for c, _ in groupby(s)) for s in strings]

# Solution: By warriors fenring76

import re


def dup(arry):
    return [re.sub(r"(.{1})\1+",r"\1",s) for s in arry]

# Solution: By warriors Blind4Basics

import re

def dup(arry):
    return list(map(lambda s: re.sub(r'(\w)\1+', r'\1', s), arry))

# Solution: By warriors FranzSchubert92

def dup(arr):
    dedup = lambda x: x[0] + ''.join(c for i,c in enumerate(x) if (i > 0 and x[i] != x[i-1]))
    return list(map(dedup, arr))
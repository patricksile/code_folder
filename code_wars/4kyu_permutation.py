# Problem:Permutation(4kyu)
"""
Instructions
"""
# My Solution:

import itertools
def permutations(str):
    return [''.join(i) for i in list(set(itertools.permutations(str)))]
# Other Solutions:

# Solution: By warriors plantpark

def permutations(s):        
    if(len(s)==1): return [s]
    result=[]
    for i,v in enumerate(s):
        result += [v+p for p in permutations(s[:i]+s[i+1:])]
    return list(set(result))

# Solution: By Edi4ka

def permutations(word):
    if len(word)<=1:
        return [word]

    perms=permutations(word[1:])
    char=word[0]
    result=[]
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return set(result)

 # Solution: By   Sebek

def permutations(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))
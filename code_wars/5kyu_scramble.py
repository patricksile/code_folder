#!/usr/bin/env python3.5
# Problem: Scramblie (5kyu)
"""
Write a function scramble(str1,str2) that returns True if a portion of str1
characters can be rearranged to match str2, otherwise returns False.

For Examples:

str1 is 'rkqodlw' and str2 is 'world' the ouput should return True.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' shoud return True.

str1 is 'katas' and str2 is 'steak' should return False.

# Only lower case letters will be used(a-z). No puctuation or digits will be
included.

# Performance needs to be considered
"""
def scramble(s1,s2):
    counter = 0
    ls1 = list(s1)
    ls2 = list(s2)
    while counter < len(ls2):
        try:
            ls1.remove(ls2[counter])
        except ValueError:
            return False
        if len(ls1) == len(list(s1)) - (counter + 1):
            counter += 1
        if counter == len(ls2):
            return True


# def scramble(s1,s2):
#     counter = 0
#     ls1 = list(s1)
#     ls2 = list(s2)
#     while counter < len(ls2):
#         if ls2[counter] in ls1:
#             ls1.remove(ls2[counter])
#             counter +=1
#             if counter == len(ls2):
#                 return True
#         else:
#             return False


# def scramble(s1,s2):
# s1 = 'rkqodlw'
# s2 = 'world'
# counter = 0
# ls1 = list(s1)
# ls2 = list(s2)
# while counter < len(ls2):
#     if ls2[counter] in ls1:
#         ls1.remove(ls2[counter])
#         print ls2[counter]
#         counter += 1
#         if counter == len(ls2):
#             return True
#     else:
#         return False


def scramble(s1,s2):
    counter = 0
    for i in set(s2):
        if i in set(s1):
            if s1.count(i) >= s2.count(i):
                counter += s1.count(i)
            else:
                return False
        else:
            return False
    if counter >= len(s2):
        return True

# I used a first condition here with issubset()

def scramble(s1,s2):
    if set(s2).issubset(set(s1)):
        counter = 0
        for l in set(s2):
            if s2.count(l) <= s1.count(l):
                counter += s2.count(l)
            else:
                return False
        if counter == len(s2):
            return True
    else:
        return False



# def scramble(s1,s2):
#     return sum(s1.count(i) if i in set(s1) else False for i in s2 ) >= len(s2)

# Other Solutions:

# Solution 1: By geneccx, paulhd

"""
# This is clever and I like it just checking if the count of the letter is lesser
# in the second string if it is not the it is obviously True.
"""

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

# Solution 2: By OOkevn

from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0

# Solution 3: By MMMAAANNN

def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))


print(scramble('cooodewwwwarrrr','codewar'))
# assert scramble('rkqodlw','world') == True
# assert scramble('cedewaraaossoqqyt','codewars') == True
# assert scramble('katas','steak') == False
# assert scramble('scriptjava','javascript') == True
# assert scramble('scriptingjava','javascript') == True

# s1 = 'katas'
# s2 = 'steak'
# ls1 = list(s1)
# ls2 = list(s2)
# print sorted(s1)
# print sorted(s2)
#  print ls1.remove(ls2[0])
# print scramble(s1,s2)
"""
Write function scramble(str1,str2) that returns true if a portion of str1
characters can be rearranged to match str2, otherwise returns false.
For example:
str1 is 'rkqodlw' and str2 is 'world' the output should return true.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
str1 is 'katas' and str2 is 'steak' should return false.
N.B: Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
"""

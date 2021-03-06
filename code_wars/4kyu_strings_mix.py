# Problem: Strings Mix (4kyu)

"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
"""
""" Full problem description https://www.codewars.com/kata/strings-mix"""
# My solution:

def mix(s1, s2):
    # a for lowercase alphabet
    a = 'abcdefghijklmnopqrstuvwxyz'
    # ct for the letter occurences
    ct = []
    for c in a:
        # sc1 and sc2 for the counts of occurences
        sc1 = s1.count(c)
        sc2 = s2.count(c)
        if sc1 > 1 or sc2 > 1:
            if sc1 == sc2:
                # inserting 0: instead of =:
                ct.append("=:{}".format(c * sc1))
            elif sc1 > sc2:
                # inserting 2: instead of 1:
                ct.append("1:{}".format(c * sc1))
            else:
                # inserting 1: instead of 2:
                ct.append("2:{}".format(c * sc2))
    # Ordering things up

    mix_s = ""
    for i in sorted(ct, key=lambda x:(len(x), x[0]), reverse=True):
        if i[0] == '0':
            mix_s += i.replace('0', '=') + '/'
        elif i[0] == '1':
            mix_s += i.replace('1', '2') + '/'
        else:
            mix_s += i.replace('2', '1') + '/'
    return mix_s[0:-1]

# My more short and explicit solution:

def mix(s1, s2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    occurences = []
    for letter in alphabet:
        s1count = s1.count(letter)
        s2count = s2.count(letter)
        if s1count > 1 or s2count > 1:
            if s1count == s2count:
                occurences.append("=:%s" % (letter * s1count))
            elif s1count > s2count:
                occurences.append("1:%s" % (letter * s1count))
            else:
                occurences.append("2:%s" % (letter * s2count))
                """
                `(-len(x), x)`
                Group the elements having same lengths and sort the groups by decreasing len(x) Inside each group, sort the elements by the "natural ordering" of x Natural ordering means that [1,2,3] < [1,2,4], [1,2,3] < [2,0,0], and [1,2,3] < [1,2,3,1]
                """
    return "/".join(sorted(occurences, key=lambda x: (-len(x), x)))


# Other Solutions

# Solution 1: By Unnamed

from collections import Counter

def mix(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    for c in set(c1.keys() + c2.keys()):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                ('2', c, n2) if n2 > n1 else ('=', c, n1))
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))

# Solution 2: By Nkrause323, Pomps, Anonym

def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))


assert(mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr")
assert(mix("looping is fun but dangerous", "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
assert(mix(" In many languages", " there's a pair of functions") == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
assert(mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo")
assert(mix("codewars", "codewars") == "")
assert(mix("A generation must confront the looming ", "codewarrs") == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")


# s1 = "A generation must confront the looming "
# s2 = "codewarrs"
# "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "looping is fun but dangerous"
s2 = "less dangerous than coding"
# "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
print(mix(s1, s2))
# mix(s1, s2) -->

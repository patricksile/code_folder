# Problem:
"""
In this kata, you have to define a function named func that will take a list as input.

You must try and guess the pattern how we get the output number and return list - [output number,binary representation,octal representation,hexadecimal representation], but you must convert that specific number without built-in : bin,oct and hex functions.

Examples :

func([12,13,6,3,6,45,123]) returns - [29,'11101','35','1d']

func([1,9,23,43,65,31,63,99]) returns - [41,'101001','51','29']

func([2,4,6,8,10,12,14,16,18,19]) returns - [10,'1010','12','a']
"""
# My Solution:
# :b for binary, :o for octal and :x for hexadecimal
def func(l):
     g = sum(l) // len(l)
     return [g, "{:b}".format(g),"{:o}".format(g),"{:x}".format(g)]

# Other Solutions:
# Solution 1: By siebenschlaefer
def func(l):
    n = sum(l) // len(l)
    return [n] + [format(n, f) for f in "box"]

# Solution 2: By anter69

def func(l):
    n = sum(l) // len(l)
    return [n] + '{:b} {:o} {:x}'.format(n, n, n).split()

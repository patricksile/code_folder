#!/usr/bin/env python3.5

# Problem: Perimeter of squares in a rectangle
"""
The drawing whows 6 squares the sides of which have a length of 1,1,2,3,5,8. It's
easy to see that the sum of the perimeters of these squares is:
4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:


# Hint: See Fibonacci sequence

# Ref: http:///oeis.org/AOOO45

The function perimeter has for parameter n where n+1 the number of squares(they are
numbered from 0 to n) and returns the totat perimeter of all  the squares.


"""


def perimeter(n):
    l = [1,1]
    for i in range(2,n+1):
        l.append(l[i-2] + l[i-1])
    return sum(l) * 4


# Other Solutions:

# Solution 1: By EarlGrey

def fib(n):
    a, b = 0, 1

    for i in range(n+1):
        if i == 0:
            yield b
        else:
            a, b = b, a+b
            yield b
def perimeter(n):
    return sum(fib(n)) * 4

# Solution 2: By Lechevalier

def perimeter(n):
    a, b = 1, 2
    while n:
        a, b, n = b, a + b, n - 1
    return 4 * (b - 1)

print(fib(3))
print(perimeter(1))

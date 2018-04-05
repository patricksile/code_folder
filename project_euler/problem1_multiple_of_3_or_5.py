### Problem:
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

### My Solution:

def mul_5or3(n):
    result = 0
    for x in range(1,n):
        if x % 3 == 0:
            result += x
        elif x % 5 == 0:
            result += x
    return result

print mul_5or3(10)

### Other Solutions:

def mul_5or3(n):
    return sum([k for k in range(n) if k % 3 == 0 or k % 5 == 0]) # This will return the sum of k in the range(n) if the controls are True

print mul_5or3(1000)

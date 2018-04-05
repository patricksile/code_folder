# Problem: Sum and Multiply (7kyu)
"""
Write a function that accepts two parameters (sum and multiply) and find two numbers [x, y], where x + y = sum and x * y = multiply.

Example:

sum = 12 and multiply = 32

In this case, x equals 4 and y equals 8.

x = 4

y = 8

Because

x + y = 4 + 8 = 12 = sum

x * y = 4 * 8 = 32 = multiply

The result should be [4, 8].

Note:

0 <= x <= 1000

0 <= y <= 1000

If there is no solution, your function should return null (or None in python).

You should return an array (list in python) containing the two values [x, y] and it should be sorted in ascending order.

One last thing: x and y are integers (no decimals).

"""
# My Solution:
"""
This refers to solve the the equation system x + y = sum and x * y = multiply,
which results to the equation ax**2 + bx + c = 0, which has two solutions

X1 = (-b + sqrt(b**2 - 4ac)) / 2a and X2 = (-b - sqrt(b**2 - 4ac)) / 2a

Thus here we will have it in the form of:

X1 = (sum + sqrt(sum**2 - 4multiply)) / 2

X2 = (sum - sqrt(sum**2 - 4multiply)) / 2

"""
# My Solution:

def sum_and_multiply(s, m):

    if (s**2 - 4 * m) < 0:
        x = abs(s**2 - 4*m) + complex('j')
        y = abs(s**2 - 4*m) - complex('j')
        if x + y == s and x * y == m:
            return [x,y]
        else:
            return None
    else:
        x = int((s + (s**2 - 4 * m) ** 0.5) / 2)
        y = int((s - (s**2 - 4 * m) ** 0.5) / 2)
        if x + y == s and x * y == m:
            return sorted([x,y])
        else:
            return None

# Other Solutions:

# Solution 1: By AustinLiu

def sum_and_multiply(sum, multiply):
    if multiply == 0:
        return [0,sum]
    half = multiply / 2
    for i in range(int(half)):
        x = i+1
        if (multiply % x) == 0:
            if x + (multiply / x) == sum:
                return [x, (multiply / x) ]
    return None


# Solution 2: By belenox

def sum_and_multiply(sum, multiply):
    for x in range(sum):
        if x * (sum - x) == multiply: return [x, sum-x]
    return None

print(sum_and_multiply(s, m))

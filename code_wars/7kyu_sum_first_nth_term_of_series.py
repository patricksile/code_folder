#!/usr/bin/env python3.5
# Problem: Sum of the first nth term of series (7kyu)
"""
Your task is to write a function which returns the sum of following series up to
nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + ...

Rules:
- You need to round the answer to 2 decimal places places and return it as string
- If the given value is 0 then it should return 0.00
- You will only be given Natural Numbers as arguments.

Examples:

series_sum(1) => 1 = "1.00"
series_sum(2) => 1 + 1/4 = "1.25"
series_sum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"

"""

# My Solution:
import decimal
def series_sum(n):
    _list = []
    for i in range(1,n+1):
        _list.append(1/(3*i - 2))
    return format(sum(_list), '.2f')


def series_sum(n):
    return format(sum(1/(3*i -2) for i in range(1, n+1)), '.2f')

# Other Solutions:

# Solution 1: By  MMMAAANNN, Six64, Ninja37
def series_sum(n):
    return '{:.2f}'.format(sum(1/(3 * i + 1) for i in range(n)))

print(series_sum())

# def series_sum(n):
#     return

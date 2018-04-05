#!/usr/bin/env python3.5
# Problem: Largest 5 digit number in a series (5kyu)
"""
In the following 6 digit number: 283910
91 is the greatest sequence of 2 digits.

Complete the solution so that it returns the largest five digit number found
within the number giver. The number will be passed in as a string of only digits.
It should return a five digit integer. The number passed may be as large as 1000
digits.
"""
# My Solution:

def solution(digits):
    biggest = 0
    for i in range(len(digits)):
        if i <= len(digits) - 5:
            current = int(digits[i:i+5])
            if current > biggest:
                biggest = current
    return biggest

# Other Solutions:
# Solution 1: By MMMAAANNN, 2-up

def solution(dd):
    # This solution works with a generator passed inside the max()
    return max(int(dd[i:i+5]) for i in range(len(dd) -4))

# Solution 2: By BrookShuihuaLee

# This solution uses lambda and generator expression.
solution = lambda digits: max(int(digits[i:i + 5]) for i in range(len(digits)))

print(solution('283910723453954359453495'))

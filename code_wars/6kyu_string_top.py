# Problem: String Top (6kyu)
"""
Task

Write a function that accepts msg string and returns local tops of string from the highest to the lowest.
The string's tops are from displaying the string in the below way:

                                                      3
                              p                     2   4
            g               o   q                 1
  b       f   h           n       r             z
a   c   e       i       m          s          y
      d           j   l             t       x
                    k                 u   w
                                        v
The next top is always 1 character higher than the previous one. For the above example, the solution for the abcdefghijklmnopqrstuvwxyz1234 input string is 3pgb.

When the msg string is empty, return an empty string.
The input strings may be very long. Make sure your solution has good performance.
Check the test cases for more samples.
"""
# My Solution:
def tops(msg):
    a = lambda x: (2*(x**2) - x + 1)
    r = range(1, len(msg))
    return ''.join(msg[a(n) - 1] for n in r if a(n) <= len(msg))[::-1]

# Other Solutions:
# Solution 1: By Blind4Basics

def tops(msg):
    i,d,s = 1,5, ''
    while i < len(msg):
        s += msg[i]
        i += d
        d += 4
    return s[::-1]

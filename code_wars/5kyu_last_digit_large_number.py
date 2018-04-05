# Problem: Last Digit of A large number(5kyu)
"""
Last digit of a large number

Instructions
Output
Define a function

def last_digit(n1, n2):
  return
that takes in two numbers a and b and returns the last decimal digit of a^b. Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6.

The inputs to your function will always be non-negative integers.

Examples

last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
Remarks

JavaScript

Since JavaScript doesn't have native arbitrary large integers, your arguments are going to be strings representing non-negative integers, e.g.

lastDigit("10", "10000000000");
The kata is still as hard as the variants for Haskell or Python, don't worry.
"""
"""
Every digit 0 thru 9 has a pattern of 4 digits when raised to an exponential power. Simply divide the power by 4 and the remainder shows you where you are at in the pattern. Here are the patterns for all 10 digits. Note that remainder 1 corresponds to the first digit in the pattern and remainder 2 corresponds to the second digit in the pattern. Remainder 3 corresponds to the third digit and remainder 0 (the power is divisible by 4) corresponds to the fourth digit in the pattern. Try a few yourself using a calculator and you will get the hang of it.
"""
# My Solution:
pattern = {'0':[0,0,0,0],'1':[1,1,1,1],'2':[2,4,8,6],'3':[3,9,7,1],'4':[4,6,4,6],
'5':[5,5,5,5],'6':[6,6,6,6],'7':[7,9,3,1],'8':[8,4,2,6],'9':[9,1,9,1]}
# Other Solutions:
# Solution 1: By
def last_digit(n1, n2):
    pattern = {'0':[0,0,0,0],'1':[1,1,1,1],'2':[2,4,8,6],'3':[3,9,7,1],'4':[4,6,4,6],
    '5':[5,5,5,5],'6':[6,6,6,6],'7':[7,9,3,1],'8':[8,4,2,6],'9':[9,1,9,1]}
    pass
# assert(last_digit(4, 1) == 4)
# assert(last_digit(4, 2) == 6)
# assert(last_digit(9, 7) == 9)
# assert(last_digit(10, 10 ** 10) == 0)
# assert(last_digit(2 ** 200, 2 ** 300) == 6)
# assert(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651) == 7)

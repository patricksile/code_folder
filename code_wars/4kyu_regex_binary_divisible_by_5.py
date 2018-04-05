# Problem: Regular expression for binary numbers divisible by 5 (4kyu)

"""
Defince a regular expression which tests if a given string representing
a binary number is divisible by 5.

Examples:
# 5 divisible by 5
PATTERN.match('101') == true

# 135 divisible by 5
PATTERN.match('10000111') == true

# 666 not divisible by 5
PATTERN.match('0000001010011010') == false

Note:

This can be solved by creating a Finite State Machine that evaluate if a string
representing a number in binary base is divisible by given number.

The detailed explanation for dividing by 3 is here: https://goo.gl/VbebVq

The FSM diagram for dividing by 5 is here: https://goo.gl/w1hUuE
"""

"""
States A,B and C correspond to inputs congruent to 0,1, and 2 mod 3, respectively. Suppose that the input so far represents a multiple of 3, so that you're in state A. A 0 multiplies the current number by 2, so it's still a multiple of 3, and you're still in state A. A 1 multiplies it by 2 and adds 1, making it congruent to 1 mod 3 and putting you in state B.

If the current number is congruent to 1 mod 3, you're in state B. An input of 0 doubles the number, making it congruent to 2 mod 3 and taking you to state C. An input of 1, on the other hand, doubles the number, making it congruent to 2 mod 3, and then adds 1, making it a multiple of 3 and sending you to state A.

In the same way you can analyze what happens when the current number is congruent to 2 mod 3 and you're in state C: doubling the number makes it congruent to 4 and hence to 1 mod 3 and moves you to state B, and doubling it and adding one leaves you in state C.

Thus, the three states really are connected properly.

All of this boils down to what I see Ted has given in his answer: when you read a bit b, you're shifting the current number one place to the left, which multiplies it by 2, and then you're adding b; the FSM mimics the effect of that operation on the residue of the number mod 3.
"""
# My Solution:

import re

# PATTERN = r'^0|(101(0)*)$'
PATTERN = r'^0|(101(0)*)$'
# pattern = re.compile(PATTERN)
test_string = "0"
if re.match(PATTERN,test_string):
    print(True)
else:

    print(False)

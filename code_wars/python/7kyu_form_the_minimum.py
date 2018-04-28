"""
Form The Minimum

Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (= ignore duplicates).

Note ::
Only Positive Numbers Will be passed To the Function (> 0 ) , Neither Negatives , or Zeroes .
Examples
[1, 3, 1]  ==> 13

[5, 7, 5, 9, 7]  ==> 579

[1, 9, 3, 1, 7, 4, 6, 6, 7] ==> 134679
ALL Translation are Welcomed (In Any Language )
If you Enjoyed this Kata , Then How About Monkey With Numbers in this Series:
"""

# First Approach

def min_value(digits):

    return int(''.join(sorted(str(n) for n in set(digits))))


# Test Zone

number = [4, 8, 1, 4]

print(min_value(number)) # 123579
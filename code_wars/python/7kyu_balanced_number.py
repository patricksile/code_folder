"""
Balanced Number (Special Numbers Series #1 )

Given an number , find whether the given number is a balanced number. A balanced number is one such that the sum of all digits to the left of the middle digit(s) and the sum of all digits to the right of the middle digit(s) are equal. If the number has an odd number of digits then there is only one middle digit, e.g. 92645 has middle digit 6; otherwise, there are two middle digits, e.g. 1301 has middle digits 3 and 0. The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g. 413023 is a balanced number because the left sum and right sum are both 5.

Our kata is simple , given a positive number determine whether the number is balanced, returning the result as a string.

Input :: Output Examples ::

balancedNum (7) // return "Balanced"   .
balancedNum (959) // return "Balanced"  .
balancedNum (295591) // return "Not Balanced" .
balancedNum (27102983) // return "Not Balanced"  .
Hope you enjoy it .. Awaiting for crafting best Practice and Clever Codes ..

Enjoy Learning !!!

Zizou
"""


def balanced_num(number):

    # number in string
    number_str = str(number)

    # Sum all the digits
    number_sum = sum(int(x) for x in number_str)

    # Length of number
    number_len = len(number_str)

    # Number divider by 2
    number_div2 = number_len // 2

    # Check if length odd or even
    if number_len % 2 and number_len != 1: # Odd

        if (number_sum - int(number_str[number_div2])) % 2: return "Not Balanced"
        else: return "Balanced"
        # Check if number sum
    elif number_len % 2 and number_len != 2: #Even
        # Check if number sum
        if (number_sum - int(number_str[number_div2 - 1 : number_div2])) % 2: return "Not Balanced"
        else: return "Balanced"


    else:
        return "Balanced"



# Test Zone
n = 432

print(balanced_num(n))
# Test.describe("Sample Tests")
# Test.it("Check Balanced Number")
# test.assert_equals(balanced_num(7), "Balanced")
# test.assert_equals(balanced_num(959), "Balanced")
# test.assert_equals(balanced_num(13), "Balanced")
# test.assert_equals(balanced_num(432), "Not Balanced")
# test.assert_equals(balanced_num(424), "Balanced")

#!/usr/bin/env python3.5

# Problem: Take a Number And Sum Its Digits Raised To The Consecutive Powers
# And ... !Eureka!! (6kyu)
"""
The number 89 is the first integer with more than one digit that fulfills the
property partially introduced in the title of this kata. What's the use of
saying "Eureka"? Because this sum gives the same number.
In effect: 89 = 8^1 + 9^2
The next number in having this property is 135. 135 = 1^1 + 3^2 + 5^3

We nee a function to collect these numbers, that may receive two integers a,b
that definces the range [a, b] (inclusive) and output a list of the sorted
numbers in the range that fulfills the property described above.

sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
"""


def sum_dig_pow(a, b):

    list_a_to_b = list(range(a, b + 1))  # List from a to b(included)
    string_list = [str(x) for x in list_a_to_b]  # Convert int in str
    valid_integer = []  # Initial valid integers
    for string in string_list:
        integers_in_string = []  # Initial sub-list of integers in string
        for index, digit in enumerate(string, start=1):
            integers_in_string.append(int(digit) ** index)  # Append digit powered with index
        if sum(integers_in_string) == list_a_to_b[string_list.index(string)]:
            valid_integer.append(sum(integers_in_string))  # Appending the sum of integers in string
    return valid_integer


print(sum_dig_pow(1, 136))


# Akuli Solution:


def sum_dig_pow(a, b):
    def filter_lelnums(iterable):
        result = []

        for number in iterable:
            number2 = 0
            for index, digit in enumerate(str(number), start=1):
                number2 += int(digit)**index
            if number == number2:
                result.append(number)

        return result
    return list(filter_lelnums(range(a, b + 1)))


print(sum_dig_pow(100, 200))

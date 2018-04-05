#!/usr/bin/env python3.5

# Finding pattern of text without Regular Expressions

# First alternative.


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        # isdecimal returns True if string contains only decimal numbers
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number: ')
print(isPhoneNumber('Moshi moshi'))

# Second alternative

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# Finding Patterns of text with regular Expressions

# Matching Regex objects

import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# Grouping with parantheses

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
print('Phone number found: ' + mo.group(1))
print('Phone number found: ' + mo.group(2))
print(mo.groups())  # returns all the separate parantheses
areaCode, mainNumber = mo.groups()
print('areaCode: {0} \nmainNumber: {1}'.format(areaCode, mainNumber))

# Matching Multiple Groups with the Pipe |

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())  # returns the first occurence of the matching text.

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
print(mo.groups())


# Optional Matching with the question mark "?"

batRegex = re.compile(r'Bat(wo)?man')  # (wo)? => "wo" is an optional group
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
# "?" => like match zero or one of the group preceding this question mark
phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# Matching zero or more with the start '*'
# "*" => matches zero or more the group preceding the star mark
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# Matching one or more with the plus '+'
# "+" => matches one or more the group preceding the plus mark
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

# Matching Specific Repetitions with Curly Brackets
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)

# Greedy and Nongreedy Matching with Curly Brackets
greedyHaRegex = re.compile(r'(Ha){3,5}')  # Will match 5 by default
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')  # Will match 3 by default
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# The findall() method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Matches all recurrences and returns them in a list
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

# Character Classes
"""
\d shorthand for the regular expression(0|1|2|3|4|5|6|7|8|9), other shorthands
\d (Any numeric digit from 0 to 9.)
\D (Any character that is not a numeric digit from 0 to 9)
\w (Any letter, numeric digit, or the underscore character.)
\W (Any character that is not a letter, numeric digit or the underscore character)
\s (Any space, tab, or newline character.)
\S (Any character that is not a space, tab, or newline)
"""
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids')
print(mo)

# Making your own character Classes

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD. aeiouAEIOU')
print(mo)

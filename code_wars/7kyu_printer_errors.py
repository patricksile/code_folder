#!/usr/bin/env python3.5
# Problem: Printer Errors(7kyu)
"""
In a factory a printer prints labels for boxes. For one kind of boxes the Printer
has to use colors which, for the sake of simplicity, are named with letters from
a to m.

The colors used by the printer are recorded in a control string. for example a
"good" control string would be "aaaabbbbhaijjjm" meaning that the printer used
three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad"
control string is produced e.g.: "aaaxbbbbyyhwawiwjjwwm".

You have to write a function printer_error which given a string will output
the error rate of the printer as a string representing a rational whose numberator is the number of errors and the denominator the length of the control string. Don't
reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from
a to z.

#Examples:

s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"
"""

# My Solution:
"""
chr(i)
Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord().
"""
def printer_error(s):
    colors = 'abcdefghijklm'
    count = 0
    for i in s:
        if i not in colors:
            count += 1
    return str(count) + "/" +str(len(s))

def printer_error(s):
    return str(sum(1 for i in s if i not in 'abcdefghijklm'))+'/'+str(len(s))

def printer_error(s):
    return "{}/{}".format(sum(1 for i in s if i not in 'abcdefghijklm'),len(s))

def printer_error(s):
    return '%s/%s'%(sum(1 for i in s if i not in 'abcdefghijklm'),len(s))

print(printer_error('aaaxbbbbyyhwawiwjjjwwm'))
# Other Solutions:

# Solution 1: by NaMe613

from re import sub
# Exploiting the regular expression sub(pattern,rpl,string) which return a string
# with the matched pattern in the string replaced by rpl(which is "" here)

def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

# Solution 2: by asmgf, dsmoker
# Learned here that the unicode makes it possible to compare letters position
def printer_error(s):
    return '%s/%s' % (sum(1 for c in s if c > 'm'), len(s))

print(len(sub("[a-m]",'','aaaxbbbbyyhwawiwjjjwwm')))

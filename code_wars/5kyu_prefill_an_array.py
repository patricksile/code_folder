#!/usr/bin/env python3.5

# Problem: Prefill an Array
"""
Create the function `prefill` that returns an array `n` elements that all have the same value `v`, See (if you can do this without using a loop).

You have to validate input:

. `v` can be anything(primitive or otherwise)
. if `v` is ommited, fill the array with `undefined`
. if `n` is 0, return an empty array
. if `n` is anything other than an integer or ### integer-formatted string(e.g.
`123` that is `>=0`, throw a `TypeError`)

When throwing a `TypeError`, the message should be `n is invalid`.
where you replace `n` for the actual value passed to the function.

Code Examples:
<code>
prefill(3, 1) --> [1,1,1]

prefill(2, "abc") --> ['abc','abc']

prefill("1",1) --> [1]

prefill(3, prefill(2,'2d')) --> [['2d','2d'],['2d','2d'],['2d','2d']]

prefill("xyz", 1) --> throws TypeError with message "xyz is invalid"
</code>
"""
# My Solution:

def prefill(n,v=""):
    if str(n).isdigit(): # isdigit() checks strings are ascii decimal digits
        return [v] * int(n)
    else:
        return "%s is invalid" % (n)

# Other Solutions:

# Solution 1: By HEXecutive

def prefill(n=0,v=None):
    try:
        return [v] * int(n)
    except:
        raise TypeError(str(n) + ' is invalid')
        
print(prefill(2,3))

# Solution 2: By jseliga

def prefill(n, v=None):
    if not str(n).isdigit():
        raise TypeError("{0} is invalid".format(n))

    return [v for i in range(0, int(n))]
"""
From the example test cases:

try: prefill('xyz', 1)
except Exception as err: value=err
Test.assert_equals(type(err), TypeError,"prefill did not throw the correct error")
Test.assert_equals(str(err), "xyz is invalid","prefill did not throw the correct error")

The tests should be:
Test.assert_equals(type(value), TypeError,"prefill did not throw the correct error")
Test.assert_equals(str(value), "xyz is invalid","prefill did not throw the correct error")
"""

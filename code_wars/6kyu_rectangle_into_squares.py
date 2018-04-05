# Problem: Rectangle into Squares (6kyu)

"""
The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

alternative text

Can you translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length (parameter named lng)
a positive integer width (parameter named wdth)
You will return an array with the size of each of the squares.

Shell bash returns a string.

  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]
#Note: lng == wdth as a starting case would be an entirely different problem and the drawing is planned to be interpreted with lng != wdth. See kata, Square into Squares. Protect trees!.

When the initial parameters are so that lng == wdth, the solution [lng] would be the most obvious but not in the spirit of this kata so, in that case, return None/nil/null/Nothing. Return {} with C++. Return the string "nil" with Bash.

In that case the returned structure of C will have its sz component equal to 0. (See the "Solution" and "Examples" tabs)

  sqInRect(5, 5) should return None
"""
# My Solution:

def sqInRect(l, w):
    if l == w: return None
    squares = []
    i = 0
    while True:
        squares.append(min(l,w))
        l = abs(l - w); w = squares[i]
        if min(l, w) == 0: break
        i += 1
    return squares

print(sqInRect(10,3))
# Other Solutions:
# Solution 1: By MMMAAANNN

# Recursive solution
def sqInRect(lng, wdth, recur = 0):
    if lng == wdth:
        return (None, [lng])[recur]            # If this is original function call, return None for equal sides (per kata requirement);
                                               # if this is recursion call, we reached the smallest square, so get out of recursion.
    lesser = min(lng, wdth)
    return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1)

# Solution 2:By g964

def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    if lng < wdth:
        wdth, lng = lng, wdth
    res = []
    while lng != wdth:
        res.append(wdth)
        lng = lng - wdth
        if lng < wdth:
            wdth, lng = lng, wdth
    res.append(wdth)
    return res

# Solution 3: by anter69

def sqInRect(a, b):
    if a == b:
        return None

    res = []

    while b:
        b, a = sorted([a, b])
        res += [b]
        a, b = b, a-b

    return res

# Solution 4: By Blind4Basics

def sqInRect(lng, wdth):
    if lng == wdth: return None
    x, y = sorted([lng, wdth])
    ans = []
    while x > 0:
        ans.append(x)
        x, y = sorted([x, y-x])
    return ans

# Solution 5: By hiasen

def sqInRect(lng, wdth):
    return _sqInRect(lng, wdth) if lng != wdth else None

def _sqInRect(lng, wdth):
    mi, ma = sorted((lng, wdth))
    return [] if 0 in (mi, ma) else [mi] + _sqInRect(ma-mi, mi)

# Solution 6: By MMMAAANNN

sqInRect=s=lambda a,b,r=0:(None,[a])[r]if a==b else [min
                           (a,b)]+s(min(a,b),abs(a-b),1)

# Problem: Persistent Bugger
"""
Persistent Bugger.

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
"""
# My Solution:
def persistence(n):
    if n < 10: return 0
    counter = 1
    while True:
        lst = list(str(n))
        m = eval(("1" + (" * {}") * len(lst)).format(*lst))
        if len(str(m)) > 1:
            n = m
        else:
            return counter
        counter += 1

print(persistence(0))

# Other Solutions:
# Solution 1: By eyaltra, Silver-Core

import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

# Solution: By bensenberner

def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist
# Solution: By Richy_s

from operator import mul
def persistence(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1
# Solution: By Kharmanoid, Jaswanth

def persistence(n):
    if n < 10: return 0
    mult = 1
    while(n > 0):
        mult = n%10 * mult
        n = n//10
    return persistence(mult) + 1
# Solution: By crbruns

def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count
    # your code
# Solution: By ylxx

persistence = lambda n,c=0: persistence(reduce(lambda x,y:int(x)*int(y),str(n)),c+1) if n >=10 else c
# Soltution: By panosgia87

def persistence(n):
    if str(n) == 1:
        return 0
    count = 0
    while len(str(n)) > 1:
        total = 1
        for i in str(n):
            total *= int(i)
        n = total
        count += 1
    return count
# Soltution: By koutoftimer

from operator import mul

def persistence(n, res=0):
    return persistence(reduce(mul, map(int, str(n))), res+1) if n > 9 else res
# Soltution: By Edwin.01

def persistence(n, result=0):
    if len(str(n)) == 1:
        return result
    else:
        return persistence(reduce(lambda x, y: int(x) * int(y), str(n), 1), result + 1)
# Soltution: By cepe, anvatar

from operator import mul
def persistence(n):
    return 0 if n < 10 else 1 + persistence(reduce(mul, map(int,str(n)))
)

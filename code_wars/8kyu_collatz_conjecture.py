# Problem: Collatz Conjecture(3n + 1) (8kyu)
"""
The Collatz conjecture (also known as 3n+1 conjecture) is a conjecture that applying the following algorithm to any number we will always eventually reach one:

[This is writen in pseudocode]
if(number is even) number = number / 2
if(number is odd) number = 3*number + 1
#Task

Your task is to make a function hotpo that takes a positive n as input and returns the number of times you need to perform this algorithm to get n = 1.

#Examples

ipdb.set_trace()  ######### Break Point ###########
hotpo(1) returns 0
(1 is already 1)

hotpo(5) returns 5
5 -> 16 -> 8 -> 4 -> 2 -> 1

hotpo(6) returns 8
6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

hotpo(23) returns 15
23 -> 70 -> 35 -> 106 -> 53 -> 160 -> 80 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#References

Collatz conjecture wikipedia page: https://en.wikipedia.org/wiki/Collatz_conjecture

"""

def hotpo(n):
    if n == 1:
        return 0
    count = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            count += 1
        elif n % 2 != 0:
            n = 3 * n + 1
            count += 1
    return count

# Other Solutions:

# Solution 1: By Zebulan and Programmerani
def hotpo(n):
    cnt = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n / 2
        cnt += 1
    return cnt

print(hotpo(23))

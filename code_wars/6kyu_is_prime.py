# Problem: Is Prime (6kyu)
"""
Is Prime

Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Example

isPrime(5)
=> true
Assumptions

You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
"""
# My Solution:
def is_prime(num):
    if num in [0,1, -1]:return False
    return all(False if num % i == 0 else True for i in range(2, int(abs(num) ** 0.5 + 1)))

def is_prime(num):
    return num > 1 and not any(num % i == 0 for i in range(2, int(num ** 0.5 + 1)))

def is_prime(num):
    # 2 and 3 will never pass in the loop it will start at range(2,3)
    return num > 1 and all(num % i for i in range(2, int(num ** 0.5 + 1)))

# Other Solutions:

# Solution 1: By nevin, shig, guest_vuff0wqxio

def is_prime(num):
    return num > 1 and not any(num % n == 0 for n in range(2,num))

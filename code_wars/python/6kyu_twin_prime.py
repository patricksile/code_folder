# Problem:
"""

"""
# My Solution:
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True
def is_twinprime(n):
    if is_prime(n) and (is_prime(n + 2) or is_prime(n -2)): return True
    return False

def is_prime(num):
    if num < 2: return False
    return all(False if num % i == 0 else True for i in range(2, int(num ** 0.5) + 1))
def is_twinprime(n):
    return True if is_prime(n) and (is_prime(n + 2) or is_prime(n -2)) else False

print(is_twinprime(25))

# Other Solutions:
# Solution 1: By

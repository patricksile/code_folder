#!/usr/bin/env python3.5
# Problem: Factorial Factory (7kyu)
"""
In mathematics, the factorial of integer 'n' is written as 'n!'. It is equal to the product of n and every integer preceding it. For example: 5! = 1 x 2 x 3 x 4 x 5 = 120.
Your mission is simple: Write a function that takes an integer 'n' and returns
'n!'.
You are guaranteed an integer argument. For any values outside the positive range,
return None.
Note: 0! is always equal to 1. Negative values should return None.
"""
# My solution:


memfact = {0: 1, 1: 1, 2: 2}


# def factorial(n):
#     if n < 0:
#         return None
#     elif memfact.get(n, -1) == -1:
#         memfact[n] = factorial(n - 1) * n
#     return memfact[n]
#
#
# print(factorial(100))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return factorial(n - 1) * n


# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return (fib(n - 1) + fib(n - 2))

# mem = {0: 0, 1: 1}
#
#
# def fib(n):
#     # global mem
#     if mem.get(n, -3) == -3:
#         mem[n] = fib(n - 1) + fib(n - 2)
#     return mem[n]
#
#
# print(fib(900))
#
def fibo(num):
    first = 0
    second = 1
    result = [0]
    print('Fibonacci series is')
    for i in range(0, num):
        third = first + second
        # print(second)
        result.append(second)
        first = second
        second = third
    print(result)
    return


print(fibo(9))

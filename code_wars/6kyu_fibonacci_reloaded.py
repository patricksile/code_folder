# Problem: Fibonacci Reloaded(6kyu)
"""
And here is Fibonacci again. This time we want to go one step further. occurences
fib() function must be faster! Can you do it?

In case you don't know. what the Fibonacci number is:

The nth Fibonacci number is defined by the sum of the two previous Fibonacci
numbers. In our case: fib(1) == 0 and fib(2) == 1. With these initial values you
should be able to calculate each following Fibonacci number.
"""

# My solution:

# Base case

fib_mem = {0: 1, 1: 0, 2: 1}
def fib(n):
    # The get() method of dictionary object is used here to avoid a KeyError
    if fib_mem.get(n, -5) == -5:            # is n(key) in the fib_mem(dict)
        fib_mem[n] = fib(n - 1) + fib(n - 2)
    return fib_mem[n]


def fib(n):
    mlist = [1, 0, 1]
    if n < 3:
        return mlist[0: n + 1]
    for i in range(3, n):
        mlist.append(mlist[i - 2] + mlist[i - 1])
    return mlist

# Other solutions:

# Solution 1: by Wenima

# This solution looks like mine but without the get(), (simpler)


fib_mem = {0: 1, 1: 0, 2: 1}


def fib(n):

    if n in fib_mem:
        return fib_mem[n]
    fib_mem[n] = fib(n - 1) + fib(n - 2)
    return fib_mem[n]


# Solution 2: by pramurugan


def fib(n):
    l = [0, 1]
    # l.extend([0, 1])
    for i in range(2, n):
        l.append(l[i - 2] + l[i - 1])
    return l

# Solution 3: by Disassembler0


# def fib(num):
#     tmp = [0, 1]
#     for _ in range(num - 1):
#         tmp[0], tmp[1] = tmp[1], sum(tmp)
#     return tmp[0]

x = 3

print(fib(x))

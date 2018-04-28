# Problem: Happy Numbers (5kyu)

"""
A happy number is a number defined by the sum of the squares
of its digits, and repeat the process until the number equals 1.
Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers (or sad numbers)(Wikipedia).
For example number 7 is happy because after a number of steps the computed sequence ends up with a 1: [7, 49, 97, 130, 10, 1]
While 3 is not, and would give us an infinite sequence.
[3, 9, 81, 64, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, 58, 89, 145, 42, 20, 4, 16, 37, 58, 89,
145, 42, 20, 4, 16, 37, 58, 89...]
Write a function that takes n as parameter and return true if and only if n is an happy number.

Happy coding!
"""


# An approach:

def is_happy(n):

    while n > 1:

        # # Decomposing n
        # n_decomposed = list(str(n))

        # # Square decomposed n
        # square_n_decomposed = map(lambda z: int(z) ** 2, n_decomposed)

        # # Sum of the squared n decomposed
        # sum_square_n_decomposed = sum(square_n_decomposed)
        
        # # Change n value
        # n = sum_square_n_decomposed

        n = sum(map(lambda z: int(z) ** 2, list(str(n))))
        print(n)
        if n == 4: return False
        # print(n)

    return True

def is_happy2(n):

    while n > 4:

        n = sum(int(z) ** 2 for z in str(n))
    
    return n == 1

# Test Zone

x = 13438

print(is_happy2(x))

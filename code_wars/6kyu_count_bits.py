### Problem: Bit Counting (6kyu)
"""
##Write a function that takes an (unsigned) integer as input, and returns
#the number of bits that are equal to one in the binary representation of that number.

#Example: The binary representation of 1234 is 10011010010,
#so the function should return 5 in this case
"""
### My Solution:

def countBits(n):
    b = 0   # b is the counter set for binaries sum.
    while n > 0:
        b += n % 2  # b incrementation with the modulus of n % 2 which gives the remainder.
        n = n // 2  # n variable reseted by doing a floor division (//) which discards the decimal part.
    return b


print (countBits(167))

### Other Solutions:

## Solution 1:

def countBits(n):
    """
    bin() methods converts an integer and returns a string
    of binary numbers and array.count("1") returns the nber
    of occurences of "1" in the string.
    """
    return bin(n).count("1") #

## Solution 2:

def countBits(n):
    # Here is a list comprehension using bin() to evaluate an integer to binary removing his 2 first characters since bin() converts to something like 0bXXX format where in this case the 0b is not needed.
    return len([x for x in str(bin(n))[2:] if x == '1'])

## Solution 3:

def countBits(n):
    """
    len() returns the lenght of a string, which will be converted by bin() first
    and returned from the string "0b..." by removing the first 2 characters "0b" which
    is obtained after each integer to binary convertion with bin() and all the "0" will
    be replaced by "" so the lenght can only count the ones in the string.

    """
    return len(bin(n)[2:].replace('0', ''))

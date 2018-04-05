# problem: emirps (5kyu)
"""
if you reverse the word emirp you will have the word prime. that idea is relatedwith the purpose of this kata.
we should select all the primes that when reverse are a different prime. the palindromic primes should be discarded.
for example: 13, 17 are prime numbers and the reversed respectively are 31, 71 which are also primes, so 13 and 17 are emirps but seee the cases, 757, 787, 797, these are palindromic primes, with the special property that primes coincides with the reversed ones, so they do not enter in the sequence.

you should create a function find_emirp(), that receives one argument n , as an upper limit and the output should be an array with this structure:
[number of emirps bellow n, largest emirp smaller than n, sum of all the emirps of the sequece bellow n]

let's some examples:

find_emirp(10) -------> [0, 0, 0] # no emirps for this value of n

find_emirp(50) -------> [4, 37, 98] # there are 4 emirps [13, 17, 31, 37]), the max. value is 37, and the sum = 13 + 17 + 31 + 37 = 98

find_emirp(100) ------> [8, 97, 418] # there are 8 emirps [13, 17, 31, 37, 71, 73, 79, 97], 97 is the highest emirp for this range and the sum of all these 8 emirp primes is 418.

happy coding!

(advise: do not use a primality test. it will make your code very slow. create a set of primes using a prime generator or a range of primes producer. remember that search in a set is faster that in a sorted list or array) (the emirps sequence is registered in oeis as a006567)
"""
def is_prime(num):

    if num < 2:
        return False
    # See if num is divisible by any number up to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_sieve(n):

    sieve = [True] * n
    # 0 and 1 are not prime numbers
    sieve[0], sieve[1] = False, False

    # Create the Sieve
    for i in range(2, int(n**0.5) + 1):
        pointer = i * 2
        while pointer < n:
            sieve[pointer] = False
            pointer += i
    # Compile the list of primes
    primes = []
    for i in range(n):
        if sieve[i] == True:
            primes.append(i)
    return primes

def find_emirp(n):
    # your code goes here
    if n <= 13:
        return [0, 0, 0]
    else:
        prime = prime_sieve(n)
        emirp = [] # List of prime numbers satisfying the conditions
        for i in prime[5:]:
            r = int(str(i)[::-1]) # i reversed
            if i != r and is_prime(r):
                emirp.append(i)
    return [len(emirp), max(emirp), sum(emirp)]



# def is_prime(num):
#     """
#     # returns true if num is a prime number, otherwise false.
#     # note: generally, is_prime is slower than prime_sieve().
#     # all numbers less than 2 are not prime
#
#     """
#     if num < 2:
#         return False
#     # see if num is divisible by any number up to the square root of num
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def gen_primes(x):
#     return [i for i in range(3, x, 2) if is_prime(i)]
#
#
# print(gen_primes(30))
#
# def find_emirp(n):
#     # your code goes here
#     if n <= 13:
#         return [0, 0, 0]
#     else:
#         prime = gen_primes(n)[4:]
#         emirp = [] # list of prime numbers satisfying the conditions
#         for i in prime:
#             r = int(str(i)[::-1]) # i reversed
#             if   i != r and is_prime(r):
#                 emirp.append(i)
#     return [len(emirp), max(emirp), sum(emirp)]

print(find_emirp(500000))

# other solutions:

# solution 1: by Jake9066

def chk_prime(x):
    if x % 2 == 0: return false
    for i in range(3, int(x**0.5+1), 2):
        if x % i == 0:
            return false
    return true

def gen_primes(n):
    return [x for x in range(3, n, 2) if chk_prime(x)]

all_primes = set(gen_primes(1000000))

def find_emirp(n):
    primes = [x for x in all_primes if x < n]
    emirps = [x for x in primes if int(str(x)[::-1]) in all_primes and x != int(str(x)[::-1])]
    return [len(emirps), max(emirps), sum(emirps)]











"""# pseudocode for sieve eratosthenes:"""
# find primes up to n
#
# for all numbers a: from 2 to sqrt(n)
#   if a is unmarked then
#        a is prime
#        for all multiple of a(a<n)
#           mark multiples as composites
# all unmarked numbers are prime!



"""# another pseudocode from the sieve eratosthenes:"""
#1 create and array fromm 0 to max

#2 starting at 2, delete every multiple of 2 from the array

#3 then, go back to the beginning from the next available number
# the beginning of the array.

#4 repeat this starting form the next available number at the beginning of the array

#5 do this until the square of number you are checking is greater than your max number.

#6 finally, compact the original array.




























# sieve of eratosthenes
# code by david eppstein, uc irvine, 28 feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ generate an infinite sequence of prime numbers.
    """
    # maps composites to primes witnessing their compositeness.
    # this is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    d = {}

    # the running integer that's checked for primeness
    q = 2

    while true:
        if q not in d:
            # q is a new prime.
            # yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            d[q * q] = [q]
        else:
            # q is composite. d[q] is the list of primes that
            # divide it. since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]

        q += 1

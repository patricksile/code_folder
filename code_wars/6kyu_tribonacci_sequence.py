#!/usr/bin/env python3.5
# Problem: Tribonacci Sequence (6kyu)
"""
Well met with Fibonacci bigger brother, AKA Tribonacci.
As the name may already reveal, it works basically like a Fibonacci, but summing
the last 3(instead of 2) numbers of the sequence to generate the next. And, worse
part of it regrettably I won't get to hear non-native Italian speakers trying to
pronounce it:(

S, if we are to start our Tribonacci sequence with [1,1,1] as a starting input
(AKA signature), we have this sequence: {1,1,1,3,5,9,17,31,....}

But what if we started with [0,0,1] as a signature? As starting with [0,1] instead
of [1,1] basically shifts the common Fibonacci sequence by once place, you may be
tempted to think that we would get the same sequence shifted by 2 places, but that
is not the case and we would get: {0,0,1,1,2,4,7,13,24,...}

Well, you may have guessed it by now, but to be clear: you need to create a Fibonacci function that given a signature array/list,  returns the first n elements
-signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number;
if n==0, then return an empty array/list and be ready for anything else which is not clearly specified:)

If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata
[Personal thanks to Professor Jim Fowler on Coursera for his awesome classes that
I really recommend to any math enthusiast and for showing me this mathematical curiosity too with his usual contagious passion:)]
"""

# My Solution:

def tribonacci(signature, n):
    if n in range(len(signature)):
        return signature[0:n]
    else:
        trib_list = [] + signature # new list with the signature added
        for i in range(3,n):
            trib_list.append(trib_list[i-3] + trib_list[i-2] + trib_list[i - 1])
        return trib_list

# Other Solutions:

# Solution 1: By Auaron, Abhi_Scorp, arb0rj, Amoth

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

print(tribonacci([1,1,1], 10))
assert(tribonacci([1,1,1],10) == [1,1,1,3,5,9,17,31,57,105])
assert(tribonacci([0,0,1],10) == [0,0,1,1,2,4,7,13,24,44])
assert(tribonacci([0,1,1],10) == [0,1,1,2,4,7,13,24,44,81])
assert(tribonacci([1,0,0],10) == [1,0,0,1,1,2,4,7,13,24])
assert(tribonacci([0,0,0],10) == [0,0,0,0,0,0,0,0,0,0])
assert(tribonacci([1,2,3],10) == [1,2,3,6,11,20,37,68,125,230])
assert(tribonacci([3,2,1],10) == [3,2,1,6,9,16,31,56,103,190])
assert(tribonacci([1,1,1],1) == [1])
assert(tribonacci([300,200,100],0) == [])
assert(tribonacci([5,17,13],2) == [5,17])

# Problem: Last digit symmetry(6kyu)

"""
Last digit symmetry


Instructions
Output
Consider the number 1176 and its square (1176 * 1176) = 1382976. Notice that:

a) the first two digits of 1176 form a prime.

b) the first two digits of the square 1382976 form a prime.

c) the last two digits of 1176 and 1382976 are the same.

Given two numbers representing a range, how many numbers satisfy this property within that range?

solve(2,1200) = 1, because only 1176 satisfies this property within the range 2 < n < 1200. See test cases for more examples. The upper bound for the range will not exceed 1,000,000.

Good luck!

"""



# def prime_sieve(n):

#     sieve = [True] * n
#     # 0 and 1 are not prime numbers
#     sieve[0], sieve[1] = False, False

#     # Create the Sieve
#     for i in range(2, int(n**0.5) + 1):
#         pointer = i * 2
#         while pointer < n:
#             sieve[pointer] = False
#             pointer += i
#     # Compile the list of primes
#     primes = []
#     for i in range(n):
#         if sieve[i] == True:
#             primes.append(i)
#     return primes

# print(prime_sieve(3702))



# def solve(a,b):
# 	if b < 1176: return 0
# 	if a < 1176: a = 1176
# 	primes = {'11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97'}
# 	ends = {'00', '01', '25', '76'}
# 	options = {i for i in range(a,b) if str(i)[:2] in primes and str(i)[-2:] in ends}
# 	return {j for j in options if str(j * j)[:2] in primes}.__len__()

# from itertools import count
# def solve(a,b):
# 	if b < 1176: return 0
# 	if a < 1176: a = 1176
# 	head = {'11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97'}
# 	end = {'00', '01', '25', '76'}	
# 	digits = count(1175)
# 	# options = (i for i in range(a,b) if str(i)[:2] in head and str(i)[-2:] in end)
# 	counter = 0
# 	while True:
# 		try:
# 			d = next(digits) ** 2
# 			if str(d)[:2] in head:

# 				counter += 1
# 		except StopIteration:
# 			break
# 	return counter, options


from itertools import count

PRIMES     = ['11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
SET_PRIMES = set(PRIMES)
TAILS      = ['00', '01', '25', '76']        # 2 digits numbers that fulfill the condition 11(76)*11(76) = ...(76)

def solve(a,b):
    maxMissingDigits = len(str(b))-4
    matches = 0
    cache = []
    for nd in range(maxMissingDigits+1):
        for p in PRIMES:
            if nd == maxMissingDigits and int(p + '0'*(nd+2)) > b:                # All next generated numbers would be > b, so break
                break 
            for t in TAILS:
                digs = count(0)
                while True:
                    d = ("{:0"+str(nd)+"}").format(next(digs)) if nd else ''     # Digits to insert in the middle of the number
                    val = int(p+d+t)                                              # val = 2 digits prime + missing digits (up to maxMissingDigits) + 2 digits tail
                    if val > b or len(d) > nd: break                              # Generated value is too high or if the digits to insert exceed the current number of digits sought for, break
                    if str(val**2)[:2] in SET_PRIMES and a <= val:
                    	cache.append(val)
                    	matches += 1
                    if not d: break                                               # If no digits to insert, the loop has to be broken manually after its first iteration
    return matches, cache

print(solve(1176, 3000))
# assert(solve(2,1200) == 1)
# assert(solve(2,100000) == 247)
# assert(solve(2,1000000) == 2549)
# assert(solve(100000,1000000) == 2302)
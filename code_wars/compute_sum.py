# Problem: Twisted Sum (6kyu)

"""
Find the sum of the digits of all the numbers form 1 to N (both ends
included).
Examples:
For N = 10 the sum is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46
For N = 11 the sum is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) = 48
For N = 12 the sum is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
"""


def compute_sum(n):
    # First case for n == 0
    if n == 0:
        return 0
    elif n <= 9:
        return sum(range(1, n + 1))
    elif n > 9:
        sum_n_9 = 45
        counter = 1
        twisted_sum_n = sum([int(i) for i in list(str(n))])
        while counter <= twisted_sum_n:
            sum_n_9 += twisted_sum_n
            counter += twisted_sum_n
        return sum_n_9


print compute_sum(11)

# cases = ((1, 1), (2, 3), (3, 6), (4, 10), (10, 46))
# for inp, res in cases:
#     assert compute_sum(inp) == res

#!/bin/env python3.5

# Problem: Sum of Pairs (5kyu)

"""
Given a list of integers and a single sum value, return the first two values (parse from left please) in order of apperance that add up to form the sum.
Negative numbers and duplicate numbers can and will appear.
NOTE: There will also be lists tested of lengths upwards of 10,0000,000 elements. Be sure your code doesn't time out.
Examples:
sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]

"""
# My Solution: In Collaboration with Zaab1t and __Myst___ on #learnpython

"""
Do substraction of `s` and the index at which I am in `ints`.
Use  sorted() or sort() also reverse them depending on the situation, set() also. some if in set or list or sorted something. To return the corresponding
value that matches with the index in `ints` and the value of the index also.
"""




# print(sum_pairs([11,3,7,5], 10))
# print(sum_pairs([4,3,2,3,4], 6))
# print(sum_pairs([0,0,-2,3], 2))
# print(sum_pairs([10,5,2,3,7,5], 10))
# print(sum_pairs([2,2], 4))
#
# print(sum_pairs([11,3,7,5], 10))
# print(sum_pairs([4,3,2,3,4], 6))
# print(sum_pairs([0,0,-2,3], 2))
# print(sum_pairs([10,5,2,3,7,5], 10))
# print(sum_pairs([2,2], 4))

# def sum_pairs(ints, s):
#     gap_list = []
#     for value in set(ints): # I just changed the list to a set.
#         if (s - value) in ints[ints.index(value) + 1 : ]:
#             gap = ints[ints.index(value) + 1 : ].index(s - value)
#             gap_list.append([gap, value, s - value])
#     if gap_list != []:
#         return min(gap_list)[1:]
#     return None

def sum_pairs(ints, s):
    # seen_set = set()
    seen_list = []
    for i in ints:
        # if (s - i) in seen_set:
        if (s - i) in seen_list:
            print(seen_list)
            return [s - i, i]
        seen_list.append(i)
        # seen_set.add(i)




# def sum_pairs(ints, s):
#     seen_set = set()
#     for i in ints:
#         seen_set.add(s - i)
#         if (s - i) in seen_set:
#             return ()
#     return (i, s - i)
        # seen_set.add(i)


# Other Solutions:

# Solution 1: By dermon12

# def sum_pairs(ints, s):
#     bla = set()
#     try:
#         return filter(lambda x: x != None ,[[s-x, x] if s-x in bla else bla.add(x) for x in ints])[0]
#     except: return None


l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]


print(sum_pairs(l1, 8)) # [1, 7]
print(sum_pairs(l2, -6)) # [0, -6]
print(sum_pairs(l3, -7)) # None
print(sum_pairs(l4, 2)) # [1, 1]
print(sum_pairs(l5, 10)) # [3, 7]
print(sum_pairs(l6, 8)) # [4, 4]
print(sum_pairs(l7, 0)) # [0, 0]
print(sum_pairs(l8, 10)) # [13, -3]

# assert(sum_pairs(l1, 8)) == [1, 7]
# assert(sum_pairs(l2, -6)) == [0, -6]
# assert(sum_pairs(l3, -7)) == None
# assert(sum_pairs(l4, 2)) == [1, 1]
# assert(sum_pairs(l5, 10)) == [3, 7]
# assert(sum_pairs(l6, 8)) == [4, 4]
# assert(sum_pairs(l7, 0)) == [0, 0]
# assert(sum_pairs(l8, 10)) == [13, -3]
# ===== Time Function ======

# t0 = time.time()
# for n in range(1, 100000):
#     sum_pairs(ints, s)
# t1 = time.time()
# print("Time required: ", t1 - t0)

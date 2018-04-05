# Problem:Build a pile of cube (6kyu)
"""
Instructions
"""
# My Solution:
from itertools import count
def find_nb(m):
	x = 0
	n = 0
	nth = count(1)
	while x < m:
		a = next(nth)
		x += (a**3)
	if x == m: return a
	elif x > m: return -1

def find_nb(m):
	x, n = 0,0
	while x < m:
		x += (n**3)
		n += 1
	if x == m: return n - 1
	return -1


print(find_nb(100))

# test.assert_equals(find_nb(4183059834009), 2022)
# test.assert_equals(find_nb(24723578342962), -1)
# test.assert_equals(find_nb(135440716410000), 4824)
# test.assert_equals(find_nb(40539911473216), 3568)
# test.assert_equals(find_nb(26825883955641), 3218)
# Other Solutions:

# Solution: By warriors

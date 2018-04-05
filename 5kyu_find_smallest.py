# Problem:Find the smallest (5kyu)
"""
Find the smallest

Instructions
Output
You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in the number, remove this digit at that index and insert it back to another place in the number.

Doing so, find the smallest number you can get.

#Task: Return an array or a tuple depending on the language (see "Your Test Cases" Haskell) with

1) the smallest number you got
2) the index i of the digit d you took, i as small as possible
3) the index j (as small as possible) where you insert this digit d to have the smallest number.
Example:

smallest(261235) --> [126235, 2, 0]
126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0

smallest(209917) --> [29917, 0, 1]

[29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than 
index `i` in [29917, 0, 1].
29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave 029917 which is the number 29917.

smallest(1000000) --> [1, 0, 6]
"""
# My Solution:

def smallest(n):    
	   
    n_list = list(str(n)); n_0 = n_list[0]

    s_0 = sorted(n_list)[0]; s_1 = sorted(n_list)[1]; 

    r_n_list = n_list[:]; r_n_list.reverse(); n_list_max = max(n_list)

    if n_list[0] != n_list_max and '0' == n_list[1] and n_list.count('0') == 1:

    	del n_list[0]; n_list.insert(1, n_0); print(n_0)

    	return [int(''.join(i for i in n_list)), 0, 1]



    if n_list[0] == n_list_max and ('0' not in n_list or '0' == n_list[1]):

    	del n_list[0]; n_list.append(n_list_max)

    	return [int(''.join(i for i in n_list)), 0, len(n_list) - 1]

    if s_0 < n_list[0] or s_0 == n_list[0] and n_list.count(s_0) > 1:

    	previous = len(r_n_list) - 1 - r_n_list.index(s_0)

    	del n_list[previous]

    	n_list.insert(0, s_0)

    	return [int(''.join(i for i in n_list)), previous, 0]

    else:

    	previous = len(r_n_list) - 1 - r_n_list.index(s_1)

    	del n_list[previous]

    	n_list.insert(1, s_1)

    	return [int(''.join(i for i in n_list)), previous, 1]
    
def smallest(n):
	pass
n = 13861 #=> [9386537932774287211, 1, 0] should equal [1386537932774287219, 0, 17] what about [1913865379327742872]
# zipping = (zip(list(str(n)), [i for i in range(len(str(n)))]))
listing = list(zip([int(i) for i in str(n)], [pos for pos in range(len(str(n)))], [list(str(n)).count(digit) for digit in list(str(n))]))

# dictionary = dict(zip(list(str(n)), [i for i in range(len(str(n)))]))
# tuppling = tuple(zip(list(str(n)), [i for i in range(len(str(n)))]))
# Test Zone
print(listing, min(listing), max(listing))
# print(smallest(187863002809))  # => [18786300289, 10, 0]
# print(smallest(5698769)) # => [5669879, 5, 1]
# print(smallest(199819884756)) # => [119989884756, 4, 0]
# print(smallest(285365)) # => [119989884756, 4, 0]
# print(smallest(935855753)) # => [358557539, 0, 8] but I got [393585575, 8, 0]
# print(smallest(94883608842)) # => [9488368842, 6, 0] but I got [48836088492, 0, 10]
# print(smallest(935855753)) # => [358557539, 0, 8] but I got [358557593, 0, 8] 
# print(smallest(903865379327742872)) # => [93865379327742872, 1, 0] should equal [38653793277428729, 0, 17]
# print(smallest(507641491557832273)) # => [76414915578322739, 0, 17] should equal [57641491557832273, 0, 1]
# Other Solutions:
cas0 = 888888 # => 888888 # count of digit == len of number: return same number
cas1 = 6918385 # => 1698385 # Min not at pos 0 and Max not at pos 0 : put far most Min at pos 0
cas2 = 1698385 # => 1369885 # Min at pos 0 and unique, 2nd min at pos(1)
cas2 = 1691385 # => 1169385 # Min at pos 0 and not unique, far most Min at pos 0 or 1 doubting
cas3 = 1169397 # => 1136997 # Min at pos 0 and not unique, but consecutive, 2nd far most min at pos(+1 in front of the far most min at the right)
cas4 = 9147568 # => 1475689 # Max at pos 0 and Min at pos 1(ignore multiple Min): put Max at pos -1
cas5 = 9417568 # => 1947568 # Max at pos 0 and Min not at pos 1: put Far most Min at pos 0


# Solution: By warriors

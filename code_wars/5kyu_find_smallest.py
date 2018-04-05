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
    


print(smallest(187863002809))  # => [18786300289, 10, 0]
print(smallest(5698769)) # => [5669879, 5, 1]
print(smallest(199819884756)) # => [119989884756, 4, 0]
print(smallest(285365)) # => [119989884756, 4, 0]
print(smallest(935855753)) # => [358557539, 0, 8] but I got [393585575, 8, 0]
print(smallest(94883608842)) # => [9488368842, 6, 0] but I got [48836088492, 0, 10]
print(smallest(935855753)) # => [358557539, 0, 8] but I got [358557593, 0, 8] 
print(smallest(903865379327742872)) # => [93865379327742872, 1, 0] should equal [38653793277428729, 0, 17]
print(smallest(507641491557832273)) # => [76414915578322739, 0, 17] should equal [57641491557832273, 0, 1]
# Other Solutions:

# Solution: By warriors

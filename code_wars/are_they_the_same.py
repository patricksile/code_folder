# Problem: Are they the same (6kyu)
"""
### Given two arrays a and b write a function 'comp(a, b)' that checks weither
# the two arrays have the "same" elements, with the same muliplicities.
## N.B: "Same" means, here that the elements in b are the elements in a squared, regardless of the oder.
## Example: Valid Arrays ====> a = [121, 144, 19, 161, 19, 144, 19, 11] ; b = [121, 14641, 20736, 361, 25921, 361,20736, 361]
## comp(a, b) returns false if the check from a to b are not the same even by one step.
## Remarks: a or b might be '[]' (all languages). a or b might be nil or null or None (except in Haskell, Elixir, C++, Rust) comp(a,b) will return false
## Remarks: a or b are nil (or null or None). the problem doesn't make sense so return false.
## Remarks: if a or b are empty the result is evident by itself
"""
#### My Solution:

def comp(array1, array2):
    if array1 == None or array2 == None: # Checks if array1 or array2 are of value None.
        return False
    if len(array1) != len(array2): # Checks if the arrays are of the same lenght.
        return False
    for x,y in zip(sorted(array1),sorted(array2)): # Returning sorted arrays while zipping them in tuple (x,y).
        return y == x**2 # Checking if y is equal to x squared


a1 = [4, 2, 1]
a2 = [1, 16, 4]
print (comp(a1, a2))


#### Best solutions:

## Solution 1:

def comp(array1, array2):
    if array1 == None or array2 == None: # Checks if array1 or array2 are of value None.
        return False
    return sorted(map(lambda x: x**2, array1)) == sorted(array2) # using map to reconstruct the list "array1" by applying the lambda function to each of his indexes, then returning two sorted list with sorted() and using the "==" to compare both and the return in the begining just give True or False depending on the Operator.
    # return sorted(x**2 for x in array1) == sorted(array2) # Good option also better than mapping in some situations

## Solution 2:

comp=lambda a,b:a!=None!=b and{n*n for n in a}==set(b)  # set() returns a sorted list with each unique element.


a1 = [4,2,1]
a2 = [1,16,4]
print (comp(a1,a2))


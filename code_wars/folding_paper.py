### Problem of Folding your way to the moon
# This code is about writing a function 'fold_to' that will return the number of time you will have to fold a paper
# to reach a given 'distance'in meter, knowing that the 'thickness' of the paper is 0.0001m.
## If somebody gives a negative distancce the function 'fold_to' should return None.
## If somebody gives a value which is positive and inferior or equal to the initial thickness of the paper 'fold_to'
## should return 0.

### Simplest case: if the paper is 1m tchick and it is fold 'four times' the it will be 8m thus with a thickness of 1m will
# have to be fold 4 times to give 16m.

def fold_to(distance):
    if distance < 0:   # Checking if the distance is positive
        return None    # None if distance is negative
    if distance < 0.0001:
        return 0 # 0 if distance is lesser than 0.0001
    if distance > 0.0001:    # Checks if distance is a greater than 0.0001
        n = 0 # store the first index in the geometric progression.
        geo_pro = [] # geo is for geometric and pro is for progression.
        while 0.0001 * 2**n <= distance: # checking if the wanted sequence number in the geo_pro is true.
                geo_pro.append(0.0001 * 2**n) # 0.0001 is the initial value and 2 is the ratio
                n = n + 1
        return len(geo_pro) # lenght of the geometric progression


print fold_to(0.0001) # Lame testing but it works after calling the function .





##### Some complex solutions for me from codewars:

### Solution 1.
import math
def fold_to(d):
    if d<0:
        return None
    if d<0.0001:
        return 0
    return math.ceil(math.log(d/0.0001,2)) # math.ceil() math.log

#### Solution 2.
from math import ceil, log
def fold_to(d):
    return None if d<0 else max(0, ceil(log(d/0.0001,2)))

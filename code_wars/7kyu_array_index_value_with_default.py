### Problem: Retrieve array value by index with default. (7Kyu)
"""
Complete the solution, It should try to retrieve the value of the array at the index
provided. if the index is out of the array's max bounds then it should return the
default value instead.
"""
### My Solution:

# def solution(items, index, default_value):
#     return (value if items[index] == value else default_value for value in items)

def solution(items, index, default_value):
    try: # Starting a try-except to control IndexError error.
        if items[index] in items:
            return items[index]
    except IndexError: # excepting the error here in case the index is out of bound
        return default_value # returning the default value

rng = list(range(1, 4))
print rng
print solution(rng, -7, 'a')
assert solution(rng, 1, 'a') == 2
# def solution(items, index, default_value):
#     len_items = len(items)
#     range_items_values = range(-len_items, len_items)
#     if index in range_items_values:
#         return items[index]
#     else:
#         return default_value

### Other Solutions:

## Solution 1:
def solution(items, index, default_value):
    try:
        return items[index] # From here I understand there is no need for a if condition.
    except IndexError:
        return default_value

## Solution 2:

def solution(items, index, default_value):
    # Here -len(items) <= index < len(items), boundaries aproach.
    return items[index] if -len(items) <= index < len(items) else default_value


## Solution 3:

def solution(items, index, default_value):
    try:
        return items[index]
    except LookupError: # This try- except catches a an error called LookupError which covers IndexError and KeyError.
        return default_value

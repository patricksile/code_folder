


### My solution:

## Long version of get_sum()
# def get_sum(a,b):
#     if a == b:
#         return a
#     else:
#         return ((max(a,b) - min(a,b)) + 1) * (a + b) / 2

# def get_sum(a,b):
#     return a if a == b else ((max(a,b) - min(a,b)) + 1) * (a + b) / 2

### Other clever solutions:

def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))

print get_sum(1, 0)  , "// 1 + 0 = 1"
print get_sum(1, 4)  , "// 1 + 2 = 6"
print get_sum(0, 1)  , "// 0 + 1 = 1"
print get_sum(1, 1)  , "// 1 Since both are same"
print get_sum(-1, 0) , "// -1 + 0 = -1"
print get_sum(-1, 2) , "// -1 + 0 + 1 + 2 = 2"

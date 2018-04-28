from itertools import chain, zip_longest
# Problem: Alternationg sort (6kyu)

"""
Write a function
alternate_sort(l)
taht combine the elements of an array by sorting the elements ascending by their absolute value and outputs negative and non-negative integers alternatingly (starting with the negative value, if any).

E.g:
alternate_sort([5, -42, 2, -3, -4, 8, -9]) == [-3, 2, -4, 5, -9, 8, -42]
alternate_sort([5, -42, 2, -3, -4, 8, 9]) == [-3, 2, -4, 5, -42, 8, 9]
alternate_sort([5, 2, -3, -4,8, -9]) == [-3, 2, -4, 5, -9, 8]
alternate_sort([5, 2, 9, 3, 8, 4]) == [2, 3, 4, 5, 8, 9]
"""

def alternate_sort(l):

    # sorted list in ascending order
    l = sorted(l, key = abs)

    # negative list
    n = list(filter(lambda x: x < 0, l))

    # positive list
    p = list(filter(lambda x: x >= 0, l))

    # range size
    len_p = len(p)
    len_n = len(n)
    range_size = max(len_p, len_n)
    
    # result list
    result = []

    for i in range(range_size):

        #append negative
        if i < len_n:
            result.append(n[i])
        if i < len_p:
            result.append(p[i])
    
    return result


    
    # return list(map(lambda y: y, sorted(l, key = abs)))

def alternate_sort2(l):

    #sort l
    l = sorted(l, key = abs)

    # negative and positive
    n, p = [i for i in l if i < 0], [i for i in l if i >= 0]

    return list(chain(*zip_longest(n, p)))

# Test zone

h = [5, -42,0, 2, -3, -4, 8, -9,-88]

print(alternate_sort2(h))
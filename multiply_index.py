def multiply_index( arr, multiplier):

    new_list = []
    for i in range(len(arr)):

        new_list.append(arr[i] * multiplier)
    
    return new_list

def dispatcher ( arr, multiplier):

    if len(arr) == 0: 
        return []

    new_list = [arr.pop(0) * multiplier]
    new_list += dispatcher(arr, multiplier)
    return new_list
    
# Test zone

array = [4, 3, 9, 8]
m = 3
print (dispatcher(array, m)) # => [12, 9, 27, 24]
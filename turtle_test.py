def no_repeat (list_1):
    # list_1 = [4,3,5,1,7,4,3,8,3,4]
    set_1 = set(list_1) 
    return sum (set_1) * 2 - sum (list_1)

#test zone
a = [5, 4, 3, 1, 2, 4, 5]
print(no_repeat(a))
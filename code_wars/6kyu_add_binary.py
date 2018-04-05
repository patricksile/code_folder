def add(a,b):
    a = '0b' + a
    b = ' + 0b' + b
    c = a + b
    print(c)
    d = eval(c)
    return bin(d)[2:]

print(add('111','10'))
assert(add('111','10') == '1001')
assert(add('1101','101') == '10010')
assert(add('1101','10111') == '100100')
assert(add('10111','001010101') == '1101100')
assert(add('00','0') == '0')

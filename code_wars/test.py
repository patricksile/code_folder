def title_case(t, m_w = ''):
    t_s = t.lower().split()
    if m_w:
        t_0 = t_s[0].capitalize() + ' '
        return t_0 + ' '.join(l if l in m_w.lower() else l.capitalize() for l in t_s[1:])
    return ' '.join(l.capitalize() for l in t_s)

print(title_case(''))
assert(title_case('') == '')
assert(title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings')
assert(title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows')
assert(title_case('the quick brown fox') == 'The Quick Brown Fox')


def rgb(r, g, b):
    round = lambda x: max(0, min(x, 255))
    return "%.2X" * 3 % (round(r), round(g), round(b))
# print(rgb(0,0,0))
# assert(rgb(0,0,0) == "000000")
# assert(rgb(1,2,3) == "010203")
# assert(rgb(255,255,255) ==  "FFFFFF")
# assert(rgb(254,253,252) ==  "FEFDFC")
# assert(rgb(-20,275,125) ==  "00FF7D")


# def square_digits(num):
#     num_str = str(num)
#     return int(''.join(str(int(i)**2) for i in num_str))
#
def square_digits(num):
    num_str = str(num)
    i = 0
    square = ''
    while i < len(num_str):
    	square += str(int(num_str[i]) ** 2)
    	i += 1
    return int(square)

# then reverse it.
#2 option
#append the result in a new string
#join all and convert it back in int
#loop through it and square it
#loop with a while loop
#split it or list it
#stringify it
#stringify the integer
{
'0':[0,0,0,0],
'1':[1,1,1,1],
'2':[2,4,8,6],
'3':[3,9,7,1],
'4':[4,6,4,6],
'5':[5,5,5,5],
'6':[6,6,6,6],
'7':[7,9,3,1],
'8':[8,4,2,6],
'9':[9,1,9,1]
}


def stringy(size):
	return '10' * ((size - 1) // 2) + '1' if size % 2 else '10' * (size // 2)
print(stringy(2))

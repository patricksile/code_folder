# Problem:
"""
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
Example:

solution(1000) # should return 'M'
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.

More about numeral numerals - http://en.wikipedia.org/wiki/Roman_numerals
"""
# My Solution:

def solution(number):
	"""This version is weird cause nothing should
	be repeated more than 3 times in the row"""

	print('%r'%number)
	numeral = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
	unit = int('1' + '0' * (len(str(number)[1:])))
	res = '' # Init. of result
	while number:
		first_digit = number // unit	# first digit in number(number).

		if first_digit > 3:
			options = first_digit - 5 # different options (4,5,6,7,8,9).
			if options == -1:
				res += numeral[unit] + numeral[5 * unit]

			elif options == 0:
				res += numeral[5 * unit]

			elif options < 4:
				res += numeral[5 * unit] + numeral[unit] * options

			elif options == 4:
				# print(first_digit,'%r => first_digit in if')
				res += numeral[unit] + numeral[unit * 10]
		else:
			res += first_digit * numeral[unit]

		number -= first_digit * unit # removing one unit off number.
		unit //= 10 # removing a zero behind the unit
	return res

# Refactored version

def solution(number):

	res = ''; number = str(number)
	numeral = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
	unit = int('1' + '0' * (len(number[1:])))

	while number != '':
		# first_digit = number // unit
		first_digit = int(str(number)[0])

		if first_digit > 3:
			options = first_digit - 5
			if options == -1: res += numeral[unit] + numeral[5 * unit]

			elif options == 0: res += numeral[5 * unit]

			elif options < 4: res += numeral[5 * unit] + numeral[unit] * options

			elif options == 4: res += numeral[unit] + numeral[unit * 10]
		else: res += first_digit * numeral[unit]

		number = number[1:]
		unit //= 10

	return res

def solution(number):
	romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
	units = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	roman_str = ''
	for i in range(len(units)):
		while number >= units[i]:
			roman_str += romans[i]
			number -= units[i]
	return roman_str


print(solution(2476)) #MMCDLXXVI

# test.assert_equals(solution(1),'I', "solution(1),'I'")
# test.assert_equals(solution(4),'IV', "solution(4),'IV'")
# test.assert_equals(solution(6),'VI', "solution(6),'VI'")

# Other Solutions:
# Solution 1: Byheworstpossiblename, Cod3r, AndersFriis, palvx

def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

# Solution: By kurnos, sandeep patel

vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))

def solution(n):
    if n == 0: return ""
    return next(c + solution(n-v) for c,v in vals if v <= n)

# Solution: By groot, Rydgel, fsanchez, lowicz

anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rnums = "M CM D CD C XC L XL X IX V IV I".split()

def solution(x):
    ret = []
    for a,r in zip(anums, rnums):
        n,x = divmod(x,a)
        ret.append(r*n)
    return ''.join(ret)

# Solution: By klox

def solution(n):
    dic = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    roman = ''
    for a in reversed(sorted(dic.keys())):
        while (a <= n):
            n = n - a;
            roman = roman + dic[a];
    return roman

# Solution: By anter69

units = " I II III IV V VI VII VIII IX".split(" ")
tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
thousands = " M MM MMM".split(" ")

def solution(n):
    return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]

# Solution: By JBuitelaar

def small(val,i,v,x):
    if val==4:
        return i + v
    if val==9:
        return i + x
    if val>5:
        return v+small(val-5,i,v,x)
    return i*val

def solution(n):
    retVal=''
    count,n=divmod(n,1000)
    if count:
        retVal+='M'*count
    count,n=divmod(n,100)
    retVal+=small(count,'C','D','M')
    count,n=divmod(n,10)
    retVal+=small(count,'X','L','C')
    retVal+=small(n,'I','V','X')
    return retVal

# Solution: By betegelse

def solution(n):
    ROMAN_SYMBOLS = ["M", "D", "C", "L", "X", "V", "I"]
    ROMAN_VALUES = [1000, 500, 100, 50, 10, 5, 1]
    idx = 0
    roman = []
    while n > 0:
        if n < ROMAN_VALUES[idx]:
            idx += 1
            continue
        n -= ROMAN_VALUES[idx]
        roman.append(ROMAN_SYMBOLS[idx])
        if roman[-4:].count(roman[-1]) == 4:
            roman = roman[:-3] + [ROMAN_SYMBOLS[idx-1]]
            if roman[-3:-2] == roman[-1:]:
                roman = roman[:-3] + [ROMAN_SYMBOLS[idx]] + [ROMAN_SYMBOLS[idx-2]]
    return "".join(roman)

# Solution: By anter69

def solution(n):
    return  " M MM MMM".split(" ")[n//1000] + \
            " C CC CCC CD D DC DCC DCCC CM".split(" ")[n//100%10] + \
            " X XX XXX XL L LX LXX LXXX XC".split(" ")[n//10%10] + \
            " I II III IV V VI VII VIII IX".split(" ")[n%10]

# Solution: By Leyto

def solution(n):
    # TODO convert int to roman string
    dictionnaire = {10**0: "I", 5*10**0: "V",
              10**1: "X", 5*10**1: "L",
              10**2: "C", 5*10**2: "D",
              10**3: "M"}
    # I define this dictionnary to simplify comprehension and visualisation

    n=str(n)
    # I make it str because I'll use power of ten to make it easier

    n=n[::-1]
    # to use only one parameter, for power of ten and incrementations

    nb_rom = ''


    for i in range(len(n))[::-1]:
        #right to left by using powers of ten

        current=int(n[i])
        #pick up caracters one by one
        if current<4:
            # 3 times the same sequence of caracter (III for example)
            nb_rom += current * dictionnaire[10**i]
            # we add the corresponding symbol

        elif current==4:

            nb_rom += dictionnaire[10**i] + dictionnaire[5*10**i]

        elif current<9:
            # works with 5,6,4,7,8
            temp = current-5
            # we wille do V+temp*I for example so we need to know how it's higher
            nb_rom += dictionnaire[5*10**i] + temp*dictionnaire[10**i]

        else:
            #current==9
            nb_rom += dictionnaire[10**i] + dictionnaire[10**(i+1)]
            # we add the current unity and the next one
            #example 9: I(10**0)X(10**1)
    return nb_rom

# Solution: By kromeasdf

def solution(n):

    dict = zip([1000,900,500,400,100,90,50,40,10,9,5,4,1 ], ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"])
    str = []

    for ar, rom in dict:
        res = divmod(n,ar)
        str += rom*res[0]
        n = res[1]

    return "".join(str)

# Solution: By Cryonic

def solution(n):
    numerals = [[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]
    final = ''
    for i in numerals:
        t = n/(i[0])
        if str(i[0])[0] == '1':
            if t >= 1 and t <= 3:
                final += (i[1]*t)
        else:
            if t >= 1:
                final+=(i[1])
        n -= i[0]*t
    return final

# Solution: By merroth1

def solution(n):
    numeral = ''
    number = [1000, 900, 500, 400, 100, 90, 50, 40, 10,9,5,4,1]
    numerals = ['M','CM','D','CD','C','XC','L', 'XL','X','IX','V','IV','I']
    print(numerals)
    square = lambda x, y: int(x/number[y]) * numerals[y]
    for i in range(13):
        numeral+= square(n, i)
        n = n - number[i]*int(n/number[i])
    return numeral

# Solution: By Edwin.01

SPQR = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
        (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def solution(n, result='', i=0):
    if i == len(SPQR):
        return result
    while n - SPQR[i][0] >= 0:
        result += SPQR[i][1]
        n -= SPQR[i][0]
    i += 1
    return solution(n, result, i)

# Solution: By Jeannie

def solution(n):
    result = []
    romans = "M", "CM", "D", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    arabics = 1000, 900, 500, 100, 90, 50, 40, 10, 9, 5, 4, 1
    for i in range(12):
        result.append(n//arabics[i] * romans[i])
        n = n - n//arabics[i] * arabics[i]
    return "".join(result)

# Solution: By monthepp

roman = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
            (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))

def solution(n):
    return next(r + solution(n - x) for r, x in roman if x <= n) if n > 0 else ''

# Solution: By sztanozs

def solution(n):
    print ("value - ", n)
    roman = {
        0:'',
        1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX',
        10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC',
        100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM',
        1000:'M', 2000:'MM', 3000:'MMM'
    }
    return ''.join(reversed([roman[int(str(n)[-a-1:][0])*10**a] for a in range(len(str(n)))]))


# Solution: By Anni_missa

def solution(n):
    ed = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    des = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    sot = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    tys = ["","M","MM","MMM","MMMM"]

    return tys[n // 1000] + sot[n // 100 % 10] + des[n // 10 % 10] + ed[n % 10]

# Solution: By nestedloop

numbers = [('M', 1000),('CM', 900),('D', 500),('CD', 400),('C', 100),
          ('XC', 90),('L', 50),('XL', 40),('X', 10),('IX', 9),('V', 5),('IV', 4),('I', 1)]
def solution(n):
    result = ''
    ind = 0
    while n>0:
        while n >= numbers[ind][1]:
            result += numbers[ind][0]
            n -= numbers[ind][1]
        ind+=1
    return result

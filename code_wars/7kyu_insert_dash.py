# Problem: Insert Dashes (7kyu)
"""
Write a function insertDash(num)/InsertDash(int num) that will insert dashes ('-') between each two odd numbers in num. For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
"""
# My Solution:
def insert_dash(num):
    dashed_num = ""
    for index, char in enumerate(str(num)):
        if int(char) % 2 == 0 or int(str(num)[index - 1]) % 2 == 0 or index == 0:
            dashed_num += char
        else:
            dashed_num += "-" + char
    return dashed_num

def insert_dash(n):
    return "".join( "-" + c if int(c) % 2 and int(str(n)[i - 1]) % 2 and i else c for i, c in enumerate(str(n)))


n = 31003567
print(insert_dash(n))

# Other Solutions:

# Solution 1: By CDBarros, Lincheney and More...

import re

# I don't yet get this code on (?=...) and "\1-"
def insert_dash(num):
    return re.sub(r"([13579])(?=[13579])", r"\1-", str(num))

# Solution 2: Azuaron
# I don't yet get this code on (?=...) and "\g<0>-"
def insert_dash(num):
    return re.sub(r"[13579](?=[13579])", "\g<0>-", str(num))

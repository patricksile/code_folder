# Problem:
"""

"""
# My Solution:
def order(sentence):
    s = sentence.split()
    d = {str(j):i for i in s for j in range(1, len(s) + 1) if str(j) in i}
    return " ".join(d[str(i)] for i in range(1, len(s) + 1))

from re import sub
order=lambda s:' '.join(sorted(s.split(),key=lambda a: sub(r'[a-zA-Z]','',a)))

from re import findall
order = lambda s: ' '.join(sorted(s.split(),key= lambda a: findall(r'\d', a)))

print(order("is2 Thi1s T4est 3a"))
# Other Solutions:
# Solution 1: By mikolajtr, acaccia, sewinter, fevjefvn, krzysiekb, cfure506

def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

# Solution : By ZozoFouchtra, user661443

def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

# Solution : By dcampbell22

def order(sentence):
    if not sentence:
        return ""
    result = []    #the list that will eventually become our setence

    split_up = sentence.split() #the original sentence turned into a list

    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first

    return " ".join(result)

# Solution : By Micromind

def extract_number(word):
    for l in word:
        if l.isdigit(): return int(l)
    return None

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))

# Solution: By lvsz

order = lambda xs: ' '.join(sorted(xs.split(), key=min))

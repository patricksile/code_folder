### Problem.
## Write a function toWeirdCase that accepts a string, and returns the same string with all even
# indexed characters in each word upper cased, and all odd indexed characters in each word lower cased.
# The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be
# upper cased.

# The passed in string will only consist of alphabetical characters and spaces (" "). Spaces will only be present
# if there are multiple words. Words will be separated by a single space(" ").

## Examples:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe' ####Test in pycharm

### My solution:

sentence = "should return the correct value for a single word"

def to_weird_case(sentence):
    counter = 0 # Countenr set to zero, because of the even number fact at zero-ith.
    weird_sentence = "" # This is the string we are going to return at the end.
    for character in sentence:
        if character == " " and counter % 2 == 0:
            weird_sentence += character
            counter += 1    # Incrementation that will now make each characters before a space to be uppercased.
        elif character != " " and counter % 2 == 0:
            weird_sentence += character.upper()
        else:
            weird_sentence += character.lower()
        counter += 1
    return weird_sentence

print(to_weird_case(sentence))

# print to_weird_case(w)


### Better Solution:

# to_weird_case() is splitting the sentence in words(str), now str or word goes to to_weird_case_word() as the name indicates and gets weird up by aligning it self in UpperLower... format, but here it is only one word (so it always works).
# And the join() methods are important not to have arrays returned instead.
# The lower() also in the to_weird_case_word() is not to be ommited in case of a uppercase in the initial words.
# Hope this is not too late...

def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
    # return ''.join(c if i%2 else c.upper() for i, c in enumerate(string.lower()))

def to_weird_case(string):
    print (string.split())
    return " ".join(to_weird_case_word(str) for str in string.split())

### A potential solution:
# def to_weird_case(w):
#     return ''.join([char.upper() if pos%2==0 else char.lower() for pos, char in enumerate(w)])
print (to_weird_case_word(sentence))
print (to_weird_case(sentence))
# print list(a)
# sa = list(a)
# print sa[3]
# sa_new = []
# print len(sa)
# i = 0
# while len(sa) >= i:
#     for x in sa:
#         print x
#         # if len(x) % 2 == 0:
#         #     # sa_new.append(x.upper())
#         #     print x
#     i = i + 1
# print sa_new

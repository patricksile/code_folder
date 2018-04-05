# Problem: Caesar Encryption (7kyu)
"""
You have invented a time-machine which has taken you back to ancient Rome. Caeser is impressed with your programming skills and has appointed you to be the new information security officer.

Caeser has ordered you to write a Caeser cipher to prevent Asterix and Obelix from reading his emails.

A Caeser cipher shifts the letters in a message by the value dictated by the encryption key. Since Caeser's emails are very important, he wants all encryptions to have upper-case output, for example:

If key = 3 "hello" -> KHOOR If key = 7 "hello" -> OLSSV

Input will consist of the message to be encrypted and the encryption key.

"""

# My Solution:

def caeser(message, key):

    alphabet = 2 * 'abcdefghijklmnouqrstuvwxyz'

    encryption = ""

    for char in message:

        if char in alphabet:

            encryption += alphabet[alphabet.index(char) + key]

        else:
        
            encryption += char

    return encryption.upper()



def caeser(m, k):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
    return "".join(a[a.index(i) + k] if i in a else i for i in m.upper())

message = "hello world"
key = 7
print(caeser(message, key))

# Other Solutions

# Solution 1: By CrazyMerlyn (python 2 solution)
# from string import maketrans, lowercase, uppercase
#
# def caeser(message, key):
#     return message.translate(maketrans(lowercase, uppercase[key:] + ascii_uppercase[:key]))


# Solution 2: By NaMe613 (python 2 solutions)
# from string import uppercase as ALPHA
#
# def caeser(message, key):
#     return ''.join(map(lambda x : ALPHA[(ALPHA.index(x) + key) % 26] if x in ALPHA else x, message.upper()))

# Solution 3: By 999999999

def caeser(message, key):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return "".join([a[a.index(x)+key] if x in a else x for x in message.upper()])

# Problem: Dbftbs Djqlfs (6kyu)
"""
Caesar Ciphers are one of the most basic forms of encryption. It consists of a message and a key, and it shifts the letters of the message for the value of the key.

Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.

Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, numbers, spaces, and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!
"""
# My Solution:

def encryptor(key, message):
    a = 'abcdefghijklmnopqrstuvwxyz' * 2
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
    encryption = ""
    for char in message:
        if char in a or char in A:
            if char.islower():
                encryption += a[a.index(char) + key % 26]
            else:
                encryption += A[A.index(char) + key % 26]
        else:
            encryption += char
    return encryption
def encryptor(k, m):
    # k is key, m is message, a is alphabet, A is ALPHABET, c is character
    a = 'abcdefghijklmnopqrstuvwxyz' * 2
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
    return "".join(a[a.index(c) + k % 26] if c.islower() \
    else A[A.index(c) + k % 26] \
    if c in a or c in A else c for c in m)

# Other Solutions:
# Solution 1: By warwickwang (maketrans can't import from python 3.6)

# from string import maketrans as mt, ascii_lowercase as lc, ascii_uppercase as uc
# def encryptor(key, message):
#     key %= 26
#     return message.translate(mt(lc+uc, lc[key:]+lc[:key]+uc[key:]+uc[:key]))

# Solution 2: By MMMAAANNN ()

from string import ascii_lowercase as l, ascii_uppercase as u

def encryptor(key, message):
    process = lambda x, abc: x in abc and abc[(abc.index(x) + key) % 26]
    return ''.join(process(c, l) or process(c, u) or c for c in message)

message = "Hello World!"
key = -120
print(encryptor(key, message))

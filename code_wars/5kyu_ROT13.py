#!/usr/bin/env python2
# Problem: ROT13(5kyu)
"""
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:
rot13("EBG13 rknzcyr.") == "ROT13 example.";
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
"""
#My Solution.
def rot13(message):
    # This works only for python2 and encode or decode will work
    return message.decode("rot13")



from codecs import encode
def rot13(message):
    return encode(message,"rot13")

print(rot13("EBG13"))

# Other Solutions:

# Solution 1 : By Six64

from string import ascii_lowercase as abc
from string import ascii_uppercase as ABC

def rot13(message):
    abc_message = abc + ABC
    abc_cipher = abc[13:] + abc[:13] + ABC[13:] + ABC[:13]
    return message.translate(str.maketrans(abc_message, abc_cipher))

# Solution 2: By Jolaf

from itertools import chain, izip
from string import lowercase, uppercase

ROT13 = dict(chain(izip(lowercase[:13], lowercase[13:]), izip(lowercase[13:], lowercase[:13]), izip(uppercase[:13], uppercase[13:]), izip(uppercase[13:], uppercase[:13])))

def rot13(message):
    return ''.join(ROT13.get(c, c) for c in message)

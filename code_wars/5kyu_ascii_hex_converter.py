#!/usr/bin/env python3.5
# Solution: ASCII hex converter
"""
Write a module Converter that can take ASCII text and convert it to hexadecimal.
The class should also be able to take hexacadecimal and convert it to ASCII text.

Example:
<code>
Converter.to_hex("Look mom, no hands") => "4c6f6f6b206d6f6d2c206e6f2068616e6473"

Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473") => "Look mom, no hands"
</code>
"""
# My solution:

from codecs import encode, decode

class Converter():

    # def __init__(self, h, s):
    #     self.h = hexadecimal
    #     self.s = string
    @staticmethod
    def to_ascii(h):
        return decode(h, "hex")

    @staticmethod
    def to_hex(s):
        return encode(s, "hex")

z = Converter()
print(z.to_ascii('6364'))
# Other Solutions:

# Solution 1: by g0loob, BartN, and 100 more other warriors
class Converter():
    @staticmethod
    def to_ascii(h):
        return h.decode("hex")
    @staticmethod
    def to_hex(s):
        return s.encode("hex")
# This solution will perfectly work in python 2 only since there is
# No more encode and decode in python 3  without the codecs libraries

# Solution 2: by EIOsoPolar, nkrause323

import binascii
class Converter():
    @staticmethod
    def to_ascii(h):
        return binascii.a2b_hex(h)
    @staticmethod
    def to_hex(s):
         return binascii.b2a_hex(s)

# Solution 3: By MMMAAANNN

class Converter():
    @staticmethod
    def to_ascii(h):
        return ''.join(chr(int(h[i:i + 2], 16)) for i in range(0, len(h), 2))
    @staticmethod
    def to_hex(s):
        return ''.join(hex(ord(char))[2:] for char in s)

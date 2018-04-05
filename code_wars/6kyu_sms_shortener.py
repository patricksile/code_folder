# Problem: Sms Shortener (6kyu)
"""
SMS messages are limited to 160 characters. It tends to be irritating, especially when freshly written message is 164 characters long. Your task is to shorten the message to 160 characters, starting from end, by replacing spaces with camelCase, as much as necessary.

For example:

Original message (169 chars):

No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that will be it.

Shortened message (160 chars):

No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!AndThatWillBeIt.
"""

# My Solution:

def shortener(message):
    extra = len(message) - 160
    splitted = message.split()
    return " ".join(splitted[:-extra]) + "".join(map(lambda x: x[0].upper() + x[1:], splitted[-extra:]))

# My refractored Solution:
def shortener(sms):
    e = len(sms) - 160
    s = sms.split()
    return " ".join(s[:-e]) + "".join(map(lambda x: x[0].upper() + x[1:], s[-e:]))


# Other Solutions:
# Solution 1: By Bouchert

import re
def shortener(t):
    return re.sub(r'(.) ',lambda m:m.group(1).upper(),t[::-1],len(t)-160)[::-1]

mes = "No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that will be it."

mes = 'Thereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoon'

# mes = 'SMS messages are limited to 160 characters. It tends to be irritating, especially when freshly written message is 164 characters long. SMS messages are limited to 160 characters. It tends to be irritating, especially when freshly written message is 164 characters long.'
print(shortener(mes))

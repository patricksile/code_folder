#!/usr/bin/env python3.5

# Problem: Regex Password Validation (5kyu)
""" You need to write regex that will validate a password to make sure it meets
the following criteria:

- At least six characters long
- Contains a lowercase letter
- Contains an uppercase letter
- Contains a number

Valid passords will only be alphanumeric characters.
"""

# Tutorials on regex by Ouims:

"""
Tutorial From Ouims:

<choupi17_> space(s), special character(s) should not validate
<Ouims> you're not checking that no space can be there
<choupi17_> yes I don't know how to do it I searched but nothing concrete
<Ouims> (?=
<Ouims> is making sure that there is the regular expression
<Ouims> (?! is making sure it's not there
<Ouims> with this and using the same logic of chained lookahead, you can express 'if anything other than letter/number are found, abort'
<Ouims> https://regex101.com/r/ZWbE40/4
<Ouims> note that i removed your extra dot at the beginning of the pattern (which i mentioned a lot but you never reacted)
<Ouims> that extra dot would simply compromise everything
<choupi17_> Sorry if I didn't
<Ouims> and would make your string at least 7 chars instead of 6
<Ouims> it's ok, we talk a lot in here, it's easy to miss messages
<Ouims> i also changed .* at the end to .+
<Ouims> there's no difference because the lookahead make sure they are characters so * can't match 0 times but ok i like to use + there because you never want that to match 0 times
<choupi17_> Ouims Thanks very much for the explanations and the solution.
<Ouims> np
<choupi17_> By the way  I have hard time to get the (?...) sequence
<choupi17_> By telling me here that (?! means it makes sure it is there changed a lot
<Ouims> (?=regex) is called positive lookahead, a(?=b) match a followed by b, but the lookahead makes its check without moving the 'cursor', so b wouldn't be part of the full match
<choupi17_> in many places it is just written Negative lookahead
<Ouims> correctly so
<choupi17_> which still makes me think it just looks backward
<Ouims> (?!regex) is a negative lookahead
<Ouims> nah, look ahead
<Ouims> since regex are left to right text processing, ahead = right
<Ouims> the counter part exists though
<Ouims> you have lookbehind (?<=regex) and (?<!regex) for negative one
<Ouims> (?<=a)b matches b preceded by a, but a won't be part of the fullmatch
<Ouims> basically the (?=) is 'i want'
<Ouims> so i want letter and number
<Ouims> (?!) is 'i don't want'
<Ouims> what is it that you don't want? space, comma, semi colon etc, of course naming all of these would be time consuming and not practical
<choupi17_> Waouh

<choupi17_> Thanks much
<Ouims> [a] match 'a', [^a] match anything that's not 'a'
<Ouims> so we use that
<Ouims> we don't want anything that IS NOT letter/number
<Ouims> you're most likely confused by the double negative
<Ouims> that will be ok with practic
<Ouims> e

<choupi17_> And what about the . alone or his combination with * like this .*
<Ouims> what do you mean
<Ouims> . match any character
<choupi17_> like when using (?=.*[A-Z])
<choupi17_> the: .*
<choupi17_> is it like "Matches any character 0 or many time"?
<Ouims> that's it
<Ouims> it's required because you want to check [A-Z] appears anywhere, effectively saying 'there is at least one uppercase letter'
<Ouims> to check if*

<choupi17_> when I played around with the regex some cases work with .+
<choupi17_> like here https://regex101.com/r/ZWbE40/5
<Ouims> yes because + is one or many times
<Ouims> so if the letter appear right at the start
<Ouims> you need that to match 0 times
<Ouims> for example
<Ouims> https://regex101.com/r/ZWbE40/6
<Ouims> here i changed the * to + for uppercase
<Ouims> and since your example start with an uppercase
<Ouims> it's not matching
<choupi17_> So it fails because it will try to match one or more uppercase letter at the beginning of the password?
<Ouims> no no
<Ouims> well i'm afraid explaining exactly why all of these is working the way it is is a bit too much informations for you right now
<choupi17_> Ok
<choupi17_> I will need to process the informations you already shared

"""
import re
from re import search
# My Solution:

regex=re.compile(r"""
^               # Beginning of the string
(?=.{6,})       # For at least 6 characters (.)but not newlines
(?=.*?\d)       # Check if there is at least 1 digit
(?=.*?[A-Z])    # Check if there is is at least 1  uppercase
(?=.*?[a-z])    # Check if there is is at least 1  lowercase
(?!.*[^a-zA-Z\d])   # Only alphanumeric
.+              # All characters or at least one
$               # End of the String
""", re.VERBOSE)


# regex=re.compile(r"^(?=.{6,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?!.*[^a-zA-Z0-9]).+$")

# Other Solutions:

# Solution 1: By niceguydave
from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)

# Solution 2: By AlexanderKoryagin

regex = (
    '^'            # start line
    '(?=.*\d)'     # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
    '{6,}'         # length at least 6 chars
    '$'            # end line
)

assert bool(search(regex, 'fjd3IR9')) == True
assert bool(search(regex, 'fjd3IR9')) == True
assert bool(search(regex, 'ghdfj32')) == False
assert bool(search(regex, 'DSJKHD23')) == False
assert bool(search(regex, 'dsF43')) == False
assert bool(search(regex, '4fdg5Fj3')) == True
assert bool(search(regex, 'DHSJdhjsU')) == False
assert bool(search(regex, 'fjd3IR9.;')) == False
assert bool(search(regex, 'fjd3  IR9')) == False
assert bool(search(regex, 'djI38D55')) == True
assert bool(search(regex, 'a2.d412')) == False
assert bool(search(regex, 'JHD5FJ53')) == False
assert bool(search(regex, '!fdjn345')) == False
assert bool(search(regex, 'jfkdfj3j')) == False
assert bool(search(regex, '123')) == False
assert bool(search(regex, 'abc')) == False
assert bool(search(regex, '123abcABC')) == True
assert bool(search(regex, 'ABC123abc')) == True
assert bool(search(regex, 'Password123')) == True

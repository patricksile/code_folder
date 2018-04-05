### Problem:
"""
Move the first letter of each word to the end of it, then add 'ay' to the end of
word.
"""
### My Solution:

from string import punctuation # This is the first time I am using this module
def pig_it(text):
    splitted_text = text.split() # Make text become a splited list and store it in a variable for efficiency issues.
    pig_it_text = ""    # Initialiaze and empty string pig_it_text which will be returned at the end.
    for word in splitted_text:  # Starting a for loop through the splitted list type*.
        if word in punctuation and splitted_text[0] == word:    # This is for punctuation exception and if it is the first word
            pig_it_text += word # No space in front since it is a punctuation
        elif word in punctuation: # This is for punctuation only any where else than the first place
            pig_it_text += " " + word   # A space in front of the punctuation
        if word not in punctuation:    # Store all words back together with 2 nested conditions.
            list_word = list(word)  # Store word in list type.
            first_letter_word = list_word.pop(0) # Store the first letter from the word list.
            pig_it_word = "".join(list_word) + first_letter_word + "ay" # Store the word back into a string type.
            if splitted_text[0] == word: # Control if it is the first word in splitted text.
                pig_it_text += pig_it_word  # If it is the first word in the text (no space in front)
            else:
                pig_it_text += " " + pig_it_word  # Else it is not the first word, thus a space in front
    return pig_it_text
    # Return the pig_it_text.

### Other Solutions

# Solution 1

def pig_it(text):
    lst = text.split()
    """
    First time I am to see the isalpha() method which return true if the word have
    only alphabet characters
    """
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# Solution 2

def pig_it(text):
    """
    First time I am to see the isalpha() method which return true if the word have
    only alphabet characters
    """
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

# Solution 3

import re

def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)



assert pig_it("Pig") == "igPay"
assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay"
assert pig_it("? Pig /") == "? igPay /"
print pig_it("? Pig %")

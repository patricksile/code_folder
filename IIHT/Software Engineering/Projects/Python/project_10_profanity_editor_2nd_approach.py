# Second approach of project 10  profanity editor

import requests

""" we will be using purgomalum API here for the profanity editor"""

def profanity_editor(text):

	# Checking if text has curse word(s)
	result_text = requests.get("http://www.purgomalum.com/service/containsprofanity?text=" + text) # => requests.models.Response
	if result_text.text == 'true':

		# Transferring each word in a list container
		text = text.split(' ') # => list

		# List of profane word(s)
		profane_list = [] # => list

		for word in text:

			# Checking if the word is profane.
			result_word = requests.get("http://www.purgomalum.com/service/containsprofanity?text=" + word) # => requests.models.Response
			if result_word.text == 'true':

				# Adding profane word to the profane list
				profane_list.append(word) # => NoneType

				# Take a new decent word at the place of the profane word. 
				decent_word = input("The word: " + "\"" + word + "\"" + " is a profane word, replace it with a decent word: ") # => str

				# Replacing the profane word with the decent word
				text[text.index(word)] = decent_word # => str

		# Putting the text together. 
		text = ' '.join(text) # => str

		return "This text had " + str(len(profane_list)) + " profane words, and this is the full decent text: \n" + text # => str

	else:

		return "Your text had no bad word(s)" # => str


# Simple test zone

t = "This is me fuck all the time but bullshit and shit is not all I know Thanks..."
s = "Thi is so cool I will be going to heaven soon..."
print(profanity_editor(t))
# /usr/bin/env python3.5
#mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard
#====================== Start of module webbrowser, sys, pyperclip test ==========================

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line. 
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard.
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
#====================== End of module webbrowser, sys, ptyperclip tes ==========================

#====================== Start of module requests test ==========================

import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res) # => <class 'requests.models.Response'>
res.status_code == requests.codes.ok # => True
len(res.text) # => 178981
print(res.text[:250]) # => The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare.

#====================== End of module requests test ==========================

#====================== Start of module requests test of method raise_for_status ==========================

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem %s' % (exc))

#====================== End of module requests test of method raise_for_status==========================

#====================== Start of file writing ==========================

import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb') # Always use as second arg 'wb' because of encoding issues
for chunk in res.iter_content(100000): # iter_content returns chunks of the content on each iteration of the loop avoiding memory crash even on massive files.
	playFile.write(chunk)

playFile.close()

#====================== End of file writing ==========================

#====================== Start of module bs4 test ==========================

import requests, bs4
res = requests.get('http://google.cm')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup) # => <class 'bs4.BeautifulSoup'>

# Loading html file now from the hard drive

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)

# Parsing the html file

import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
print(type(elems)) # => <class 'list'>
len(elems) # => 1
print(type(elems[0])) # => <class 'bs4.element.Tag'>
elems[0].getText() # => 'Al Sweigart'
print(str(elems[0])) # => '<span id="author"> Al Swegart</span>'
print(elems[0].attrs) # => {'id':'author'}

# Getting data from a paragraph tag

pElems = exampleSoup.select('p')
str(pElems[0]) # => '<p>Download my <strong>Python</strong> book from <a href="http://\ninventwithpython.com">my website</a>.</p>'
pElems[0].getText() # => 'Download my Python book from my website.'
str(pElems[1]) # => '<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText() # => 'Learn Python the easy way!'
str(pElems[2]) # => '<p>By <span id="author">Al Sweigart</span></p>'
pElems[2].getText() # => 'By Al Sweigart'

# Getting data from an element's attributes

soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
str(spanElem) # => '<span id="author">Al Sweigart</span>'
spanElem.get('id') # => 'author'
spanElem.get('some_nonexistent_addr') == None # => True
spanElem.attrs # =>{'id' : 'author'}

#====================== End of module bs4 test ==========================
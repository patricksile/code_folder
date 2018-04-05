# /usr/bin/env python3.5
# lucky.py - Opens several Google search results search

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page

# Get the command line arguments and request the search page

res = requests.get('http://google.cm/search?q=' + ' '.join(sys.argv[1:]))
print(type(res))
res.raise_for_status() # Check for http errors

# print(type(res.text))

# Retrieve top search result links.result
soup = bs4.BeautifulSoup(res.text)


# Open a browser tab for each result.
linkElems = soup.select('.r a') # Selecting html class= 'r' followed by anchor <a>

numOpen = min(3, len(linkElems)) # minimum number of links to open
for i in range(numOpen):
	webbrowser.open('http://google.cm' + linkElems[i].get('href'))


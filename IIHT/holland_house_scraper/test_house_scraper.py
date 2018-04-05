# /usr/bin/env python3.5
from urllib.parse import urlparse # module to clean links (built-in)
import urllib.parse
import webbrowser # Open links with a web browser(built-in)
import time # To insert some delay on actions


# open file with websites raw links
web_file = open('websites.txt','r')

# read object web_file and save in links_file
links_file = web_file.read().split('\n') #adfsdfsdfdsf

# clean_links = [] # object clean_links of the class array
clean_links = []
for link in links_file:
	clean_links.append(urlparse(link).netloc)

clean_links = [urlparse(line).netloc for line in links_file] # object clean_links of the class array
cities = ['haarlem', 'amsterdam'] # list of cities for test purpose with www.huurwoningen.nl which is the first link 

for link in clean_links[0]:

	for city in cities: # https://www.huurwoningen.nl/in/haarlem/?min_price=100&max_price=300

		for max_price in range(500, 600,100):
# 

			time.sleep(5) # 5seconds sleep or delay
			webbrowser.open("https://%s/in/%s/?min_price=%d&max_price=%d"%(link, city, 300, max_price)) # 
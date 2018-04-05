# /usr/bin/env python3.5
from urllib.parse import urlparse # module to clean links (built-in)
import urllib.parse
import webbrowser # Open links with a web browser(built-in)
import time # To insert some delay on actions
import requests
import selenium
# open file with websites raw links
web_file = open('websites.txt','r')

# read object web_file and save in links_file
links_file = web_file.read().split('\n')
# print(links_file)


clean_links = [urlparse(link).netloc for link in links_file] # object clean_links of the class array

print(clean_links)
cities = ['haarlem', 'amsterdam'] # list of cities for test 

# res = requests.get("https://www.huurwoningen.nl/in/amsterdam/?min_price=100&max_price=900") # Doesn't work



for domain in clean_links[0:1]:

	for city in cities: 

		for max_price in range(500, 601,100):
			
			time.sleep(5) # 5seconds sleep or delay
			webbrowser.open("https://%s/in/%s/?min_price=%d&max_price=%d"%(domain, city, 300, max_price)) # opening each pages in a new tab


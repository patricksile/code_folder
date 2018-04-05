# # /usr/bin/env python3.5
# from urllib.parse import urlparse # module to clean links (built-in)
# import urllib.parse
# from time import sleep
# import webbrowser # Open links with a web browser(built-in)
# import requests # Downloads files and web pages (external)
# import bs4 # Parses HTML (external) 
# import selenium # Launches and controls a web browser (external)
# import time # To insert some delay on actions
# import smtplib # To send files through smtp server
# import email.mime.text # To send data to an email

# # open file with websites raw links
# web_file = open('websites.txt','r')

# # read object web_file and save in links_file
# links_file = web_file.read().split('\n') #adfsdfsdfdsf

# # clean_links = [] # object clean_links of the class array

# clean_links = [urlparse(line).netloc for line in links_file] # object clean_links of the class array
# cities = ['haarlem', 'amsterdam'] # list of cities for test purpose with www.huurwoningen.nl which is the first link in the object list clean_links
# # page_download = requests.get("http://%s/in/%s/?min_price=%d&max_price=%d"%("www.huurwoningen.nl", "haarlem", 300, 600)).text
# # webbrowser.open("http://www.huurwoningen.nl/in/haarlem/?min_price=300&max_price=600")
# # sleep(10)
# # page_download = requests.get("https://jobs.jumia.cm/en/jobs-douala/?by=digital+marketer")
# # page_download_bs4 = bs4.BeautifulSoup(page_download.text,"lxml")

# for link in clean_links[0]:

# 	for city in cities: # https://www.huurwoningen.nl/in/haarlem/?min_price=100&max_price=300

# 		for max_price in range(500, 601,100):
# # 

# 			time.sleep(5) # 5seconds sleep or delay
# 			webbrowser.open("https://%s/in/%s/?min_price=%d&max_price=%d"%(link, city, 300, max_price)) # opening each pages in a new tab

			
# 			# page_download = requests.get("http://%s/in/%s/?min_price=%d&max_price=%d"%(link, city, 300, max_price))# downloading the page in the page_download

# 			# print(page_downlaod)
			 
# 			# page_download.raise_for_status()# http error checking

			
			# soup = bs4.BeautifulSoup(page_download.text)# creating a bs4 object for further html parsing 

			

			# price_link = soup.select('div span .linsting_price')# price link elements to select of object list

			# for i in range(len(price_link))

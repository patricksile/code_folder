# /usr/bin/env python3.5
from urllib.parse import urlparse # module to clean links (built-in)
import urllib.parse
from time import sleep
import webbrowser # Open links with a web browser(built-in)
import requests # Downloads files and web pages (external)
import bs4 # Parses HTML (external) 
import selenium # Launches and controls a web browser (external)
import time # To insert some delay on actions
import json # To write our data to a json file
import io # Make it wor for python 2 and 3




jobs = ["digital+marketer","web+designer","ingenieur"] # list of jobs
cities = ["douala","yaounde"] # list of cities

# dynamic_link_format = "https://jobs.jumia.cm/en/jobs-%s/?by=%s"%(job,city) # dynamic_link_format
test_link = "https://jobs.jumia.cm/en/jobs-douala/?by=digital+marketer"

page_download = requests.get(test_link).text # Downloaded the page

page_download_soup = bs4.BeautifulSoup(page_download) # Object BeautifulSoup of page_download
# print(page_download_soup)

job_pages = page_download_soup.select('a.icon-eye') # Fetches all links with <a class="icon-eye">... as a list object on the page


data = {} # dictionary object to store data

for job_page in job_pages[:1]:
	# webbrowser.open("https://jobs.jumia.cm" + job_page.get('href'))
	data_page = requests.get("https://jobs.jumia.cm" + job_page.get('href')).text # Downloading the page on which we want to collect data
	print(data_page)
	data_page_soup = bs4.BeautifulSoup(data_page) # Object BeautiFulSoup of data_page

	# print(data_page_soup.select('div.dl-horizontal').get_text())
	# data_page_job_description = data_page_soup.select('div.dl-horizontal') # selection of job description
	job_details_section = data_page_soup.select('.job-details-section')
	job_title_detail = data_page_soup.select('h4.dl-title') # Job title detail in a list object
	job_title_detail_info = data_page_soup.select('div.dl-horizontal') # Job details in a list object

	# print(job_details_section[0].get_text())

"""


I want to read more on bs4 module and look how I can genuinely collect the data I want on the job detail page.

- Thinking about writing some couple of functions to manage each type of informations.(But I think I should be reading the bs4 documentation to accomplish whatever)

- Thinking of making some classes that will handle some tasks

- Thinking of using regular expression, really crazy idea here, always good to be crazy

- Thinking of looking for a module that can take screenshot, another crazy one




"""

	# for index in range(len(job_title_detail)):

		# data[job_title_detail[index].get_text()] = job_title_detail_info[index].get_text() # adding job title and job title details in the object dictionary data

		# job_description_data = data_page_soup.select('div.dl-horizontal')[0].get_text() # selection of job description

	# Adding job description to the data dictionary object

	# print(data)


# print(job_pages[0].get('href'))
# for link in clean_links[0]:

# 	for city in cities: # https://www.huurwoningen.nl/in/haarlem/?min_price=100&max_price=300

# 		for max_price in range(500, 600,100):


			# time.sleep(5) # 5seconds sleep or delay
			# webbrowser.open("https://%s/in/%s/?min_price=%d&max_price=%d"%(link, city, 300, max_price)) # opening each pages in a new tab

			
			# page_download = requests.get("http://%s/in/%s/?min_price=%d&max_price=%d"%(link, city, 300, max_price))# downloading the page in the page_download

			# print(page_downlaod)
			 
			# page_download.raise_for_status()# http error checking

			
			# soup = bs4.BeautifulSoup(page_download.text)# creating a bs4 object for further html parsing 

			

			# price_link = soup.select('div span .linsting_price')# price link elements to select of object list

			# for i in range(len(price_link))

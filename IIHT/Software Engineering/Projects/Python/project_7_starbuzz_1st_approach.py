# First approach of project 7 starbuzz coffee
import urllib.request # Importing urllib.request object.
import time # importing the time object


# Starting an infinite loop which wait for a minute when the price is lower than $4.74
while True:

	# Wait a minute before making the request of the page.
	time.sleep(60)

	# Getting the url html page
	page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html") # => http.client.HTTP.Response

	# converting the data in a str object. 
	text = page.read().decode("utf8") # => str

	# Lokking for the index of the $ sign.
	index_of_dollar_sign = text.index('$') # => int

	# Retrieving the price from the page.
	price = text[index_of_dollar_sign: index_of_dollar_sign + 5] # => str

	# Checking if the price of coffee is below $4.74
	if price < '$4.74':
		# printing the price of coffee if it is below $4.74
		print(price)
		 


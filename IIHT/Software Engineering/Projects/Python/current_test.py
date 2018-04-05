# First approach of project 7 starbuzz coffee
import urllib.request # Importing urllib.request object.
import time # importing the time object


# Starting an infinite loop which wait for a minute when the price is lower than $4.74


def coffee_price(time_delay,):

	"""
		coffee_price function will take an integer objetc as time_delay representing the seconds to wait for before having the coffee price.
	"""

	# Wait a minute before making the request of the page.
	time.sleep(time_delay)

	# Getting the url html page
	page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html") # => http.client.HTTP.Response

	# converting the data in a str object. 
	text = page.read().decode("utf8") # => str

	# Lokking for the index of the $ sign.
	index_of_dollar_sign = text.index('$') # => int

	# Retrieving the price from the page.
	price = text[index_of_dollar_sign: index_of_dollar_sign + 5] # => str

	return price

while True:

	print("Choose an option to know the current coffee price.")
	option = input("Press '1' for the first option and '2' for the second option:")

	if option != '1' and option != '2':
		print("Try again please you pressed %s instead of '1' or '2'!"% option)
		continue

	else:

		if option == '1': 

			print("You selected option '1'.\nPlease wait for constant updates of the coffee price under $4.74.")
			break

		else:

			print("You selected option '2'.\nPlease wait for constant updates of the coffee price at his current price.")
			break

while True:

	if option == '1':

		# coffee price from the predefined function
		price = coffee_price(10) # => str

		# Checking if the price of coffee is below $4.74
		if price < '$4.74':
			# printing the price of coffee if it is below $4.74
			print(price)


	else:

		# coffee price from the predefined function
		price = coffee_price(10) # => str

		# printing the price of coffee at any rate.
		print(price)
			 


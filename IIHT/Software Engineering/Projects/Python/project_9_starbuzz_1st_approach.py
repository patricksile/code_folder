 # First approach of project 9 starbuzz coffee

import urllib.request # Importing urllib.request object.
import time # importing the time object

import tweepy # importing the twitter API object tweepy


# All authentications tokens from the user and the application.
consumer_key = "mKunLVzGKlyFYpcKtoVNIibaR"
consumer_key_secret = "Q1xLi6RGa9o1NoG8WsaurU2MNw7FBHu3IAlBmNkUNrq69cVmuq"
access_token = "354921961-mfT477eDRD7Q6Wd3b2IEgKMIBkNe6WlKtM3QhbLC"
access_token_secret = "gu19AxtFhoNzzD74vtZ8mrq1AHpwl1vUUvlbcc5ibCVS3"
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token,access_token_secret)

# Activating the authentications token
api = tweepy.API(auth)

# "@__yes___or___no"
# "@bnsiewe"



def coffee_price(time_delay):

	"""
		coffee_price function will take an integer objetc as time_delay representing the seconds to wait for before having the coffee price.
	"""

	# Wait a minute before making the request of the page.
	time.sleep(time_delay)

	# Getting the url html page
	page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html") # => http.client.HTTP.Response

	# converting the data in a str object.
	text = page.read().decode("utf8") # => str

	# Looking for the index of the $ sign.
	index_of_dollar_sign = text.index('$') # => int

	# Retrieving the price from the page.
	price = text[index_of_dollar_sign: index_of_dollar_sign + 5] # => str

	return price



# Receiver of the messages on Twitter
receiver = "@WanbanEdilette"
while True:

	# coffee price from the predefined function
	price = coffee_price(20) # => str

	if price < "$4.74":

		message = "Hi, Mr. CEO of SieweCoffee.\nDropped price of Coffee: %s"%price # => str

		# Sending a direct message to a twitter account
		api.send_direct_message(user=receiver, text=message)  # => NoneType
	else:

		message = "Hi, Mr. CEO of SieweCoffee.\nEmergency price of Coffee: %s"%price #=> str

		# Sending a direct message to a twitter account
		api.send_direct_message(user= receiver, text=message)
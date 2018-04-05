import os, sys
from flask import Flask, request
from pymessenger import Bot
from pprint import pprint # for pretty printing and test

# Dependencies for the starbuzz_price
import urllib.request
from time import sleep

app = Flask(__name__)


# Webhook = https://070d730f.ngrok.io
PAGE_ACCESS_TOKEN = "EAAB9U9kI7OMBAA7lVaTnLBF8ZAv4hne4RqCyMLX8XgTp1jtSI1DZAM0eN0YCYRyEd2BbBAcRrv8ToX8y7HyJEC3zrv7SIlOMg5IZAaSRXPydMZAkbfFDUUO1XN7ebLQhjmmWzYZAUZCU9iTFdXzSZCUtfR98GXKTkbMD8cwDUfeeg0CMD5L7Xiq"




# Bot instance
bot = Bot(PAGE_ACCESS_TOKEN)


# Verification settings by writing a new view

@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):

		if not request.args.get("hub.verify_token") == "696000793":
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Let's try this differently...", 200




# writing a new view

@app.route('/', methods=['POST'])

def webhook():
	# get data from the chat on messenger
	data = request.get_json()

	# print the log on the terminal screen, just for test
	log(data)

	return "ok", 200



def log(message):

	pprint(message)
	# print the complete message stored in the buffer
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)



# Sending the coffee_price to the facebook admin of the page
def coffee_price(time_delay):

	"""
		coffee_price function will take an integer objetc as time_delay representing the seconds to wait for before having the coffee price.
	"""

	# Wait a minute before making the request of the page.
	sleep(time_delay)

	# Getting the url html page
	page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html") # => http.client.HTTP.Response

	# converting the data in a str object.
	text = page.read().decode("utf8") # => str

	# Looking for the index of the $ sign.
	index_of_dollar_sign = text.index('$') # => int

	# Retrieving the price from the page.
	price = text[index_of_dollar_sign: index_of_dollar_sign + 5] # => str

	return price

# Send a text to the page
sender_id = '1530178270396594'
recipient_id = '682020518574190'
app_id = '137799076998371'


while True:

	# coffee price from the predefined function
	price = coffee_price(120) # => str

	if price < "$4.74":

		message = "Hi, Mr. CEO of StarBuzz.\nDropped price of Coffee: %s"%price # => str

		# Sending a direct message to a facebook page account
		bot.send_text_message(sender_id, message) # => NoneType
	else:

		message = "Hi, Mr. CEO of StarBuzz.\nEmergency price of Coffee: %s"%price #=> str

		# Sending a direct message to a facebook page account
		bot.send_text_message(sender_id, message)

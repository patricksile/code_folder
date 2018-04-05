import os, sys
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)


# webhook_ngrok = "https://c09f914c.ngrok.io "

# PAGE_ACCESS_TOKEN_paness = "EAACvI9ZCer2kBAIQbQQZAU94QEfpAtGb3q0dt8pWZCtrCdifZBFkaUbpZBivddN2uRprkkhw6rMh5nmtvZAZBrOPUoNKZB0hhyO6WZCOFzn9CQmR89Xh1ZAQdkJI1jCvIJmpYKd0C91dYErpeDaZCXOuyD78HRfcjG177zTDCKj7hwPIaLpgWB8Sk8o17CZCzZAj5Sz0ZD"

# Bot object
# bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):

		if not request.args.get("hub.verify_token") == "696000793":
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello World me again", 200



# writing a new view

@app.route('/', methods=["POST"])

def webhook():
	# get data from the chat on messenger
	data = request.get_json()

	# print the log on the screen
	log(data)

	# if data['object'] == 'page':
	# 	for entry in data['entry']:
	# 		for messaging_event in entry['messaging']:
	# 			# IDs
	# 			sender_id = messaging_event['sender']['id']
	# 			recipient_id = messaging_event['recipient']['id']

	# 			if messaging_event.get('message'):
	# 				if 'text' in messaging_event['message']:
	# 					messaging_text = messaging_event['message']['text']
	# 				else:
	# 					messaging_text = "no text"

	# 				# Echo
	# 				response = messaging_text

	# 				bot.send_text_message(sender_id, response)


	return "ok", 200





def log(message):

	print(message)	
	# print the complete message stored in the buffer
	sys.stdout.flush()

if __name__ == "__main__":
	app.run(debug = True, port = 80)



# nosj = {'object': 'page', 'entry': [{'id': '1173165799481941', 'time': 1512761803869, 'messaging': [{'sender': {'id': '1529452990495272'}, 'recipient': {'id': '1173165799481941'}, 'timestamp': 1512761803856, 'read': {'watermark': 1512761802128, 'seq': 0}}]}]}


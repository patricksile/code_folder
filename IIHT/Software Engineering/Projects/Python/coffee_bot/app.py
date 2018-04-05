import os, sys
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)



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

	print(message)
	# print the complete message stored in the buffer
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)




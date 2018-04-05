# Problem:Vasya Clerk (6kyu)
"""
Instructions
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change. Otherwise return NO.

###Examples:

### Python ###

tickets([25, 25, 50]) # => YES 
tickets([25, 100]) 
         # => NO. Vasya will not have enough money to give change to
"""
# My Solution:
def tickets(client):

	if client[0] != 25: return 'NO'
	b25 = []; b50 = []; j = 0
	for i in range(len(client)):
		if client[i] == 25: 
			b25.append(25); j += 1
		if client[i] == 50 and len(b25) >= 1:
			b50.append(50); b25 = b25[1:]; j += 1
		if client[i] == 100 and len(b25) >= 1 and len(b50) >= 1: 
			b25 = b25[1:]; b50 = b50[1:]; j += 1 
		if client[i] == 100 and len(b25) >= 3:
			b25 = b25[3:]; j += 1	
	return 'YES' if j == len(client) else 'NO'

def tickets(client):
	print('%r'%client)
	b25,b50,j = 0,0,0
	for i in client:
		if i == 25: b25 += 25; j += 1
		if i == 50 and b25 >= 25: b50 += 50; b25 -= 25; j += 1
		if i == 100 and b50 >= 50 and b25 >= 25: b50 -= 50; b25 -= 25; j += 1
		if i == 100 and b25 >= 75: b25 -= 75; j += 1
	return 'YES' if j == len(client) else 'NO'

print(tickets([25,25,50,50,50]))
# Other Solutions:

# Solution: By warriors
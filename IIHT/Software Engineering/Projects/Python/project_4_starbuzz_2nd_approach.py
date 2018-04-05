# Second approach Starbuzz coffee project

import urllib.request # Importing urllib.request object.
import bs4 # Importing bs4 object.

# Getting the url html page
page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html") # => http.client.HTTP.Response

# converting the data in a str object 
text = page.read().decode("utf8") # => str

# Converting the text object to a bs4.BeautifulSoup for parsing the html
text_soup = bs4.BeautifulSoup(text,'lxml') # => bs4.BeautifulSoup

# Getting the tag enclosing the price information.
price_tag = text_soup.select("p strong") # => list

# Retrieving the text between the tags to have the price of coffee.
price = price_tag[0].get_text() # => str

# Printing out the price.
print(price)


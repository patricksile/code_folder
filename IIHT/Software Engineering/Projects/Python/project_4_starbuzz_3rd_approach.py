# Third approach Starbuzz coffee project

import urllib.request # Importing urllib.request object.
import re # Importing re object for regular expressions.

# Getting the url html page
page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html") # => http.client.HTTP.Response

# converting the data in a str object. 
text = page.read().decode("utf8") # => str

# Getting the price with re object in a container.
price_list = re.findall(r'\$[0-9]*\.?[0-9]*', text) # => list

# Retrieving the  price of coffee in the container.
price = price_list[0] # => str


# Printing the result out.
print(price) 
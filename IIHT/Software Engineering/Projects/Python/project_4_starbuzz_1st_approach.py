# First approach Starbuzz coffee project

import urllib.request # Importing urllib.request object.

# Getting the url html page
page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html") # => http.client.HTTP.Response

# converting the data in a str object. 
text = page.read().decode("utf8") # => str

# Getting the index of the dollar sign in the text(str)

index_of_dollar_sign = text.index('$') # => int


# Retrieving the  price of coffee in the container text(str).
price = text[index_of_dollar_sign : index_of_dollar_sign + 5] # => str

# Printing the result out.
print(price) # => NoneType


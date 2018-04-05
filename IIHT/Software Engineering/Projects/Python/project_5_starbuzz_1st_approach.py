# First approach of project 5 starbuzz coffee
import urllib.request # Importing urllib.request object.

# Getting the url html page
page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html") # => http.client.HTTP.Response

# converting the data in a str object. 
text = page.read().decode("utf8") # => str

# Lokking for the index of the $ sign.
index_of_dollar_sign = text.index('$') # => int

# Retrieving the price from the page.
price = text[index_of_dollar_sign: index_of_dollar_sign + 5] # => str

# Printing the result out.
print(price) 
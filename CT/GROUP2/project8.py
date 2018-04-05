#GROUP2
import urllib.request
import time
import re
#coffee_price_option function declaration or definition
def coffee_price_option(option):
    while True:

        if option != '1' and option != '2':
            print(option,"n'est pas une option valide")
            option = input("Entrez  '1' pour des prix inferieur $4.74 et '2' pour le prix courant :") #=> str

            continue
            
        #wait 5 second
        time.sleep(5)
        # Open the url
        page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html") # => http.client.HTTPResponse
        # Get the content the content of page object
        text = page.read().decode('utf8') # => str
 
        #Get the price of the coffee in the html page
        prices = re.findall(r'\$\d.\d\d',text) #=> list
 
        #verifies if choice entered is one
        if option == "1":
        #verifies if current price is < $4.74                                           #print the current price
            if prices[0] < "$4.74":
                print(prices[0]) #=> NoneType                  
 
        #verifies if choice entered is two
        elif option == "2":
            print(prices[0]) #=> NoneType2
            break  

#User input choice
choice_of_the_user = input("Entrez  '1' pour des prix inferieur $4.74 et '2' pour le prix courant :")#=>str  
# Calling or Invoking the function coffee_price_option        
coffee_price_option(choice_of_the_user)

        

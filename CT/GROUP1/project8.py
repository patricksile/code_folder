#GROUP1

import urllib.request
import re
import time 

#prompting a user to choose an option
option = input('choose between option 1 and 2: ')  #type = str
#choose first option  
if option == '1':
    while True:
        #open url
        page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices-loyalty.html')   #type = http.client.HTTPResponse
        #read the html
        text = page.read().decode("utf8")   #type = str
        #extract price
        price = re.findall(r'\$\d.\d\d', text) #type = list
        #current price
        current_price = price[0] #type = str    
        #max price
        maximum_price = '$4.74' #type = str
        #
        if current_price < maximum_price:
            #print current_price
            print(current_price)        
        # Delay of 10 seconds for testing purpose
        time.sleep(2)   #type = NoneType

#choose second option 
elif option == '2':    
    #open url
    page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices-loyalty.html')   #type = http.client.HTTPResponse
    #read the link
    text = page.read().decode("utf8")   #type = str
    #extract price
    price = re.findall(r'\$\d.\d\d', text) #type = list
    #print price and emergency text
    print(price[0], 'i am out of stock please command urgently') #type = str

elif option:
    print('wrong option, option must be between 1 and 2')    
    

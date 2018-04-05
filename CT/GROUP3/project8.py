#GROUP3
# it is an extensible library for opening urls 
import urllib.request #=> module
import re
import time
# add the posibility of choice
option = input("choose option 1 or 2:")#=> str
# first option
if option == "1":#=>str
    while True:   
        # open the url
        page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")#=>http.client.Httpresponse
        text = page.read().decode("utf 8")#=>str
        # extract price
        price = re.findall(r'\$\d.\d\d',text)
        # fixed_price
        varying_price = price[0]
        fixed_price = "$4.74"
        if varying_price < fixed_price:
            print(varying_price)
            time.sleep(2)

#second option
if option == "2":
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")#=>http.client.Httpresponse
    text = page.read().decode("utf 8")#=>str
    price = re.findall(r'\$\d.\d\d',text)
    current_price = price[0]
    print(current_price)
    
# when user dont choose correct option
else:
    while True:
        option = input("choose only between 1 and 2:")#=> str
          # first option
        if option == "1":#=>str
            while True:   
        # open the url
                page= urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")#=>http.client.Httpresponse
                text= page.read().decode("utf 8")#=>str
        # extract price
                price= re.findall(r'\$\d.\d\d',text)
        # fixed_price
                varying_price= price[0]
                fixed_price = "$4.74"
                if varying_price < fixed_price:
                    print(varying_price)
                    time.sleep(2)

        #second option
        if option=="2":
            page= urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")#=>http.client.Httpresponse
            text= page.read().decode("utf 8")#=>str
            price= re.findall(r'\$\d.\d\d',text)
            current_price = price[0]
            print(current_price)
            break
        







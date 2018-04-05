#GROUP0
import urllib.request
import re
import time
choice = input('Enter your choice [1-2] : ')#=> str

while True:

    # Coffee price retrieving function 
    def price_from_page():
    # ouvrir et lire l'adresse url
        page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    #pernet d obtenir le code html
        text = page.read().decode("utf8") #=> str
    # extraire les chiffre
        price = re.findall(r"\$\d.\d\d", text)#=> list
        
        return price[0]   

    if choice == "1":
      
        while True:

            varying_price = price_from_page()
            fixe_price = '$4.74'#=> str

            if fixe_price > varying_price:

                print(varying_price)
                time.sleep(5)
        
    elif choice == "2":
        
        print(price_from_page())
        break 
        
    choice = input('Please re-enter your choice [1-2] : ')#=> str

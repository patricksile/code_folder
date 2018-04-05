# FOR THIS SCRIPT TO WORK PROPERLY MAKE SURE YOU HAVE THIS LIBRARIES INSTALLED ON YOUR PC 

###############################
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from selenium.webdriver.common import keys #the position for your keys maybe different 
import time

###################################



url = "https://www.afribaba.cm/douala/immobilier-location-vente/locations-appartement-maison/"

#use Firefox webdriver(API) to open firefox, also make Firefox a seaech object  
browser = webdriver.Chrome(executable_path=r'getko\chromedriver.exe')#executing Firefox using geckodriver

#function to preape soup #### soup is just a name given to what BeautifulSoup returns 
def prepare_soup(currentUrls):
    
    #use search object to open website
    browser.get(currentUrls)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    return soup

def get_link_cat(linkCat,soup):
    results = []
    for a in soup.find_all('a', href=re.compile(linkCat)): 
        results.append(a['href'])   # collecting houses    

    return results      
#getting the presnt link from the URl
currentPage = browser.current_url

# call soup to filter javascript
soup = prepare_soup(url)

#====================== linkks structure ==========================
# after observing the links structur of Afriba this how links  like to services are compossed.
# Under immobilier 
# this will get all house rentals in Douala 
houseRentLinkCat = 'https://www\.afribaba\.cm/douala/immobilier-location-vente/location' # house rental 
housesRental = get_link_cat(houseRentLinkCat,soup) 

houseSalesLinkCAt = 'https://www\.afribaba\.cm/douala/immobilier-location-vente/ventes'# house sales 
houseSales = get_link_cat(houseSalesLinkCAt,soup)


landSalesLinkCat = 'https://www\.afribaba\.cm/douala/immobilier-location-vente/terrain'# Land sales 
landSales = get_link_cat(landSalesLinkCat,soup)

hotelLinkCat = 'https://www\.afribaba\.cm/douala/immobilier-location-vente/hotels' # Hotel Rental 
hotels = get_link_cat(hotelLinkCat,soup)

#================  end  ==============================

StudioLinks = []
for links in housesRental:
    
    studioLinksCat = '//www\.afribaba\.cm/douala/studio'
    soup = prepare_soup(links)
    time.sleep(5)
    StudioLinks = get_link_cat(studioLinksCat,soup)  
    
    for x in StudioLinks:         
        x = x.rstrip('.html')
        browser.get(x)
        soupi = BeautifulSoup(browser.page_source, "html5lib")
        soupi = prepare_soup(x)
        time.sleep(15)
        stDetails = soupi.find('ul', class_="list-unstyled")
        print(x)
        print(stDetails)
        
print("\n \n========== House rental ==========")

                  
 
                     
                     
#results.close()     
#browser.quit()

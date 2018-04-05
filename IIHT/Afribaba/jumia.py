# FOR THIS SCRIPT TO WORK PROPERLY MAKE SURE YOU HAVE THIS LIBRARIES INSTALLED ON YOUR PC 

###############################
import codecs 
import platform
import webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from selenium.webdriver.common import keys #the position for your keys maybe different 
import time
from selenium.webdriver.support.ui import Select
import urllib.request

###################################

cities = {'Doula','Kribi','Buea', 'Yaounde'}

url = "https://house.jumia.cm/"
#webbrowser.open(url)
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

#browser.get(url)

# call soup to filter javascript
soup = prepare_soup(url)
#location = input("Where will You like to leave")
location = browser.find_element_by_id("searchbar").send_keys("Douala")
Budject = browser.find_element_by_id("maximum-price").send_keys("200000")


mySelect = Select(browser.find_element_class_name("selectkit-caret"))
mySelect.select_by_visible_text("Maison").click()


browser.find_element_by_class_name("selectkit-caret").click()


#browser.find_element_by_id("lnkSelectKit-display").send_keys("Maison")
#browser.find_element_by_xpath("//select[@name='category[]']/option[text()='Maison']").click()



StudioLinks = []
for links in housesRental:
    
    studioLinksCat = '//www\.afribaba\.cm/douala/studio'
    soup = prepare_soup(links)
    time.sleep(5)
    StudioLinks = get_link_cat(studioLinksCat,soup)
    #print(StudioLinks)
    
    for x in StudioLinks:

      


       
        x = x.rstrip('.html')
        browser.get(x)
        soupi = BeautifulSoup(browser.page_source, "html5lib")
        soupi = prepare_soup('https://www.afribaba.cm/douala/appartement-meuble-a-bonamoussadi-273522.html')
        time.sleep(15)
        stDetails = soupi.find('ul', class_="list-unstyled")
        print(x)
        print(stDetails)
        
   # print(StudioLinks)
    
    
    
    

print("\n \n========== House rental ==========")
#for links in houseSales:
  #  print(links)
                  
 
                     
                     
#results.close()     
#browser.quit()

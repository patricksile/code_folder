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
###################################

cities = {'Doula','Kribi','Buea', 'Yaounde'}

url = "https://www.afribaba.cm/"
#webbrowser.open(url)
#use Firefox webdriver(API) to open firefox, also make Firefox a seaech object  
browser = webdriver.Chrome(executable_path=r'getko\chromedriver.exe')#executing Firefox using geckodriver

#function to preape soup #### soup is just a name given to what BeautifulSoup returns 
def prepare_soup(currentUrls):
    
    #use search object to open website
    browser.get(currentUrls)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    return soup
    


#use search object to open website
browser.get(url)
#Service = browser.find_element_by_xpath


with open("results.txt","a",encoding='utf-8', errors = 'ignore') as results:
     
 #location = input("Please inpu the Town you want to search Houses in: ")
 #if location in cities:
   #  print(location)
    select = browser.find_element_by_id('category')
    for option in select.find_elements_by_tag_name('option'):
        if option.text == 'Immobilier Location - Vente':

            option.click()
            print(option)
            break
    
   # text = select.select_by_visible_text('Immobilier Location - Vente')
   # print(text)
  #  browser.find_element_by_xpath("//select[@id='category']/option[text()='Immobilier Location - Vente']").click()

 #else:
  #  print("wrong")
 

                     
                     
#results.close()     
#browser.quit()

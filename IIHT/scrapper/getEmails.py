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
###################################

url = "https://www.groupon.com/"
#webbrowser.open(url)
#use Firefox webdriver(API) to open firefox, also make Firefox a seaech object  
browser = webdriver.Chrome(executable_path=r'getko\chromedriver.exe')#executing Firefox using geckodriver

#function to preape soup #### soup is just a name given to what BeautifulSoup returns 
def prepare_soup(currentUrls):
    
    #use search object to open website
    browser.get(currentUrls)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    return soup
    
#content = unicode(q.content.strip(codecs.BOM_UTF8), 'utf-8')

#use search object to open website
browser.get(url)
#find click "no thank" button
browser.find_element_by_class_name("ls-gtg-dismiss").click()
with open("results.txt","a",encoding='utf-8', errors = 'ignore') as results:
 locationsList = open("town.txt" ,"r")
 location = locationsList.read().split('\n')
 for a in location:
          city = a

          results.write("\n\n"+city+"\n")

            #receive user service
          services = open("service.txt","r")
          read = services.read().split('\n')
          for b in read:
              service = b
                   # results = open("results.txt","w")
              results.write("\t"+b+"\n \n")

              browser.find_element_by_id("ls-search").clear() #clear value in search bar
              search_bar = browser.find_element_by_id("ls-search")#finds the the seach field for service

              #find,make and clear search location
              location = browser.find_element_by_id("ls-location").clear()

              #get search location
              loca = browser.find_element_by_id("ls-location")
              print(service)
              

              search_bar.send_keys("hotel") # sends a value into the just field

              loca.send_keys(city)#send location
              time.sleep(5)

              button = browser.find_element_by_class_name("ls-header-search-button").click() #find and click search button




              time.sleep(15)#wait for page to load 
              dealsUrl = [] #table to store links to deals
              currentPage = browser.current_url # get current page url
              
              counter = 0
              while ((currentPage != url) and (counter < 17)):
                    counter += 1 
                    url = currentPage
                    soup = prepare_soup(currentPage) #function call to prepare soup
                    for a in soup.find_all('a', href=re.compile('https://www\.groupon\.com/deals')): #getting links to deals
                            dealsUrl.append(a['href'])# adding links to table 
                     

                    while True:#result maybe display in several pages. This block check for Next Button and click it.
                       try:
                            button = browser.find_element_by_class_name('next')#check for next Button
                            button.click() #click Button
                            time.sleep(5) #wait for page to load befor continuing
                            currentPage = browser.current_url # get the url of the new page 
                       except:
                         break
                  


              for x in dealsUrl:
                    
                     browser.get(x) #function call
                     time.sleep(5) #wait for page to load
                     
                     soupi = BeautifulSoup(browser.page_source, "html5lib")#pase the severs reponse to BeautifulSoup

                     #///////// Because groupon has a copules of class to denote where the adress is, this block check in the lis of known class to get a coresponding class.
                     #///// note i am not sure this are all the classes so if a class is not here BeautifulSoup returns None.
                     Adress = soupi.find('div', class_="address-content")
                     Phone = soupi.find('div', class_="address-phone")
                     if Adress == None :
                         Adress = soupi.find('div', class_="address")
                         if Adress == None:
                             Adress = soupi.find('div', class_="merchant-location")
                             if Adress == None:
                                 Adress == soupi.find('li', class_="merchant-location-card")
                            
                                 
                      #////////////////////
                                        
                                 
                         
                     while True:# this is check to see if the Deal has a link to the company's website
                       try:
                          marchantLink = "maneh"
                          marchantProfile = soupi.find('div', class_="merchant-profile")
                          #for tag in marchantProfile:
                          marchantName = marchantProfile.find('h4')
                          NameOf = marchantName.text
                          marchanT = NameOf.strip()#marchant name without white space
                          results.write(marchanT+"\t")
                          marchant = browser.find_element_by_class_name('merchant-website') #get element merchant-website if it exist
                          marchantLink = marchant.get_attribute("href") #Extract the href property from elemt
                          
                                         
                          print("here is the Marchant Link ",marchantLink)
                          break #break out from loop
                       except:# if merchant-website does not exist it breaks out
                          break
                     if Adress != None:
                         Adress = Adress.text
                         Adresss = Adress.lstrip("About")
                         Adresss = ' '.join(Adresss.split())
                         #Adresss = re.sub('\s+',' ',Adresss)     #removing white spaceds and tabs from the addres
                       #  Adresss = Adresss.decode('latin-1', 'ignore')
                         results.write(Adresss+"\t")
                         
                             
                         print("The Adress is :", Adresss)
                     if Phone != None:
                         Phone = Phone.text
                         Phone = Phone.lstrip("Get Directions")
                        # Phone = re.sub('\s+',' ',Phone)
                         Phone = ' '.join(Phone.split())
                       #  Phone = Phone.decode('latin-1', 'ignore')
                         results.write(Phone+"\t")
                         
                         print("The Phone NUmber Is : ",Phone)
                     inResults = []   
                     if(marchantLink != re.compile("https://www.facebook.com/")):
                         if marchantLink not in inResults:
                              inResults.append(marchantLink)
                             
                              results.write(marchantLink+"\n")
                         
                    
                     
                     
results.close()     
browser.quit()

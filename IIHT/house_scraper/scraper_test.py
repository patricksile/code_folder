import html.parser # not in use
import urllib.request, urllib.parse, urllib.error #not in use
import re # not in use
import datetime # not in direct use
import mysql
from html.parser import HTMLParser # not in use
import mysql # not in use
import time # not used
import json # not used
import sys
import MySQLdb
from lxml import html
import requests
from urllib.parse import urlparse
from datetime import date, timedelta
import smtplib

def remove_non_ascii_1(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])

try:
    #connecting to the mysql server
    conn = MySQLdb.connect(host= "127.0.0.1",
                  user="root",
                  passwd="",
                  db="scrapper")
    #getting a cursor for the database
    x = conn.cursor()

    #getting the configurations data from the config table
    x.execute("""SELECT * FROM config WHERE Id=1""")
    result = x.fetchone()

    #getting the minimum price of the houses to search
    min_price = result[1]
    #getting the maximum price of the houses to search
    max_price = result[2]
    #getting the town of the houses to search
    town = result[3]

    #opening the file that contains the links
    file_content = open("links.txt", "r");

    #an array to store the links
    links = []

    data = []

    #parsing the file to get the links
    for link in file_content:
        #adding each link to the links array
        links.append(link)

    #closing the file we opened
    file_content.close()

    #final_data is the array that stores the scrape files
    final_data = []
    for url in links:

        #we parse the uri so as to get the domain name
        parsed_uri = urlparse( url )
        #getting the domain name
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        #testing the group of websites which uses the format town/minprice-maxprice
        if domain == "http://www.funda.nl/" or domain == "http://www.jaap.nl/":
            #getting the content of these sites
            page = requests.get(link.strip()+str(min_price)+"-"+str(max_price)+"/")
            print(url+str(min_price)+"-"+str(max_price) +" - starts crawling")
        #testing for those who use the format ?minimalPrice=minprice&maximalPrice=maxprice&city=city
        elif domain == "http://www.zah.nl/":
            #getting the content of these sites
            page = requests.get(url+"?minimalPrice="+str(min_price)+"&maximalPrice="+str(max_price))
            print(url+"?minimalPrice="+str(min_price)+"&maximalPrice="+str(max_price) +" - starts crawling")

        #getting the html data in the form of xml so as to parse it with XPATH
        tree = html.fromstring(page.content)

        #getting the homes names
        house_names = tree.xpath('//h3[@class="search-result-title"]/text()')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_names) == 0:
            house_names = tree.xpath('//div[@class="result"]/h2/a/text()')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_names) == 0:
            house_names = tree.xpath('//h2[@class="property-address-street"]/text()')
        #getting homes addresses
        house_addresses = tree.xpath('//small[@class="search-result-subtitle"]/text()')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_addresses) == 0:
            house_addresses = tree.xpath('//div[@class="result-content"]/p/span[@class="city"]/text()')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_addresses) == 0:
            house_addresses = tree.xpath('//div[@class="property-address-zipcity"]/text()')

        #getting prices
        house_prices = tree.xpath('//span[@class="search-result-price"]/text()')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_prices) == 0:
            house_prices = tree.xpath('//div[@class="info-price"]/text()')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_prices) == 0:
            house_prices = tree.xpath('//div[@class="property-price"]/text()')

        #getting dimensions
        house_dimen = tree.xpath('//ul[@class="search-result-kenmerken "]/li/span/text()')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_dimen) == 0:
            house_dimen = tree.xpath('//div[@class="result-content"]/ul/li[2]/text()')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_dimen) == 0:
            house_dimen = tree.xpath('//div[@class="property-features"]/div[@class="property-feature"][3]/text()')

        #getting number of rooms
        house_rooms = tree.xpath('//ul[@class="search-result-kenmerken "]/li[2]/text()')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_rooms) == 0:
            house_rooms = tree.xpath('//div[@class="result-content"]/ul/li[1]/text()')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_rooms) == 0:
            house_rooms = tree.xpath('//div[@class="property-features"]/div[@class="property-feature"][2]/text()')

        #getting images
        house_img = tree.xpath('//div[@class="search-result-image"]/img/@src')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_img) == 0:
            house_img = tree.xpath('//div[@class="result"]/a/img/@src')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_img) == 0:
            house_img = tree.xpath('//div[@class="property-photos"]/div[@class="property-photo"]/img/@src')

        #getting the link to the houses
        house_site = tree.xpath('//div[@class="search-result-header"]/a/@href')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_site) == 0:
            house_site = tree.xpath('//div[@class="result"]/h2/a/@href')
        #if no data is get from the xpath query above, then we move to the next xpath query
        if len(house_site) == 0:
            house_site = tree.xpath('//a[@class="property-inner"]/@href')

        #print house_img
        #print house_names
        #print house_dimen
        #print house_prices
        #print house_rooms
        #print house_addresses

        print(len(house_names))
        print(len(house_dimen))
        print(len(house_prices))
        print(len(house_rooms))
        print(len(house_addresses))

        i = 0
        j = 0
        k = 0
        #print house_dimen
        #final_data = []

        #now we parse all those arrays to mix an form the data needed
        for i in range(len(house_addresses)):
                #house name
                name = house_names[i].strip()

                #eliminating non ASCII cacracters
                name = remove_non_ascii_1(name)

                #getting sites names
                site = house_site[i]

                #if the domain is http://www.fundal.nl/ then we apply some particularities which it has
                if len(house_names) == 2*len(house_addresses): #domain == "http://www.funda.nl/":
                    #getting the names according to this sites display
                    name = house_names[k].strip()
                    k = k+2
                if domain == "http://www.funda.nl/":
                    #adding the domain to relative links
                    site = "http://www.funda.nl" + house_site[i]

                #getting addresses
                address = house_addresses[i].strip()
                #eliminating non ASCII cacracters
                address = remove_non_ascii_1(address)

                #getting prices
                price =house_prices[i].strip()[2:]
                #eliminating non ASCII cacracters and replacing the /mnd by blank space
                price = remove_non_ascii_1(price).replace('/mnd', r'')

                #getting dimensions
                dimen = house_dimen[i].strip()[:-1]
                #eliminating non ASCII cacracters and replacing the m by blank space
                dimen = remove_non_ascii_1(dimen).replace('m', r'').replace(' ', r'')

                #getting dimensions with the specificities of the folloqing website
                if len(house_dimen) == 2*len(house_addresses): #domain == "http://www.zah.nl/":
                    dimen = house_dimen[j].strip().replace('m', r'').replace(' ', r'')
                    j = j + 3

                #getting rooms and replacing kmers by blanck space
                rooms =remove_non_ascii_1(house_rooms[i].replace('kamers', r'')).replace(' ', r'')


                #getting pictures links
                photo = house_img[i]

                #adding tthe data to the final_data array
                final_data.append((domain, site, name, photo, address, price, dimen, "", rooms))

                #inserting data to the temp table of the database
                x.execute("""INSERT INTO temp (`Photo`, `Title`, `Description`, `Price`, `Town`, `Domain`, `Room`, `Dimen`, `Site`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """, (photo, name.replace("'", r"\\'"), "", price, address.replace("'", r"\\'"), domain, rooms, dimen, site))
                conn.commit()


    sender = 'caleblongonje@gmail.com'
    receivers = ['patouossaibrahim@gmail.com']
    #Getting the date of today
    today = time.strftime("%Y-%m-%d")
    print(today)
    #Getting the date of yesterday
    yesterday = date.today() - timedelta(1)

    #getting the data stored on the temp table
    sql = "SELECT * FROM temp"
    x.execute(sql)
    results = x.fetchall()

    #stores the new datas in the new_data array
    new_data = []

    #browsing each rows of data
    for row in results:
        title = row[1]
        price = row[3]
        #verify if the house has already been stored
        x.execute("""SELECT * FROM `houses` WHERE `Date`=%s AND `Title`=%s AND `Price`=%s LIMIT 1""", (yesterday.strftime('%Y-%m-%d'),title, price))
        verify = x.fetchall()
        if(len(verify) == 0):
            #if the house is not ye stored then it is consdered as new
            new_data.append(title)

    #if there are new data
    if len(new_data) > 0:
        html_msg = """From: From Person <from@fromdomain.com>
                        To: To Person <to@todomain.com>
                        MIME-Version: 1.0
                        Content-type: text/html
                        Subject: Daily house updates : %s """ % (today)
        for new in new_data:
            #we get house details from the temp table
            x.execute("""SELECT * FROM temp WHERE `Title`=%s LIMIT 1""", (new))
            data = x.fetchone()
            photo = row[0]
            title = data[1]
            description = data[2]
            price = data[3]
            town = data[4]
            domain = data[5]
            room = data[6]
            dimen = data[7]
            site = data[8]
            html_msg += "<div style='height:100px;'>" \
                        "<a href='"+site+"' style='display:block; width:100%; height:100%;'>" \
                            "<table border='0'>" \
                                "<tr>" \
                                    "<td>" \
                                        "<img src='"+photo+"' style='width:100px; height:100px;'/>" \
                                   "</td>" \
                                   "<td>" \
                                       "<p><big style='font-size:1.3em;'>"+title+"</big><br>" \
                                        "Price : "+price+" Euro<br>" \
                                        "Rooms : "+ room+"<br>" \
                                         "Dimensions : "+ dimen+"<br>" \
                                        "Town : "+ town+"" \
                                      "</p>" \
                                      "</td>" \
                                  "</tr>" \
                              "</table>" \
                          "</a>" \
                      "</div><br>"
            #insert the data in the houses table
            x.execute("""INSERT INTO houses (`Photo`, `Title`, `Description`, `Price`, `Town`, `Domain`, `Room`, `Dimen`, `Site`, `Date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], today))
            conn.commit()
        try:
            #smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            #smtpObj.sendmail(sender, receivers, html_msg)
            mailserver = smtplib.SMTP('smtp.gmail.com', 587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login('patouossaibrahim@gmail.com', '753football')
            mailserver.sendmail(sender, receivers, html_msg)
            print("Successfully sent email")
        except :
            print("Error: unable to send email")

except IOError:
    print("There was an error opening the file << links.txt >>")
    sys.exit()

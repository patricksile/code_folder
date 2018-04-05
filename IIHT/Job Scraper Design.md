# Job Scraper Design

I - Overview

Job Scraper tool objective is to eliminate the whole tedious repetitive manual steps that job seakers have to go through to get some job opportunities that concisely matches with their needs. The tool will practically be a web application that will be taking care to do all the automations and return results in real time to users in their respective mails.

This design document will actually be both the design with the architectures on building our Job Scraper tool.


II - Design

II - 1 General view.

1.. Get the job search websites links analyse, and store them.
2.. Collect users infos(names, location, phone, emails, etc...)(database)
3.. Based on users infos go through each job search website and collect data in real time and return it to each corresponding users by mail.
For the design, we will have the following:



II - 2 Physical design


1. Job search websites analyse

- Manually search for notorious job search websites.
- Go through each of them and check that it is a feasible to scrape them.
- Discard for the ones that might be trouble for the practicability of our tool and the one which might raise legal issues.
- Then store the valid ones in a database. 

2. Users info collection.

Build a secured(https) worldclass standard responsive web interface on which all the user - client interaction will take place.

- The first user experience with the web interface should be as smooth as possible (No unecessary aspect and informations).
{Actually the interface should even make it possible for user to just put in their emails, a name(), their job interest and location (this should be as easy as possible to do from a user experience) and that's all after validation they are linked and good to go}(I think the moment to ask for more infos should be after a user is already having a minimum service(whole customer acquisition concept), of course there should be a possibility to go for a further registration)
- Provide a secured database for the user informations.

3. Web scraping and return of results.

- Our web application should request to valid job search websites for very precise informations.
- That information should be returned to the user by mail with a desirable mail format.


II - 3 Logical design


III - Architectures
 
For the architectures, we will have the following:

1. Physical architecture
2. Logical architecture


III - 1 Physical architecture

III - 2 Logical architecture

IV - Technologies (System Architecture)

IV - 1 Client

For the web application we will use(HTML5, CSS3, JS) for its appearance and node.js as the dynamic part and for the interaction with the server. We choose node.js because it has a great documentation and is popularity.()

IV - 2 Server

For the server side we have a large variaty of options but we will go for the Google solution called FireBase, because we believe it has a perfect balance between their prices and quality of services.

IV - 3 Scraping

For the scraping automation this will be runned in Python, because so far it is among one of the best programming language that allows such task less tedious to implement.






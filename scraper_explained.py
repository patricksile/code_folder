#Open file with websites
file = open("websites.txt","r")

#read file with websites and save in file_content
file_content = file.read()
file_content = file_content.split ('\n')

#separating lines in the string
            
#Print file content to make sure , note that file_content is of type string
print(file_content)
 
#Clean urls
"""===== block to extract domains from the url ===="""
websites_domains = [] # container to store cleaned websites

#getting every url from the string object one after the other
for line in file_content :
             domain = urlparse(line).netloc #extracting domain from url
             websites_domains.append(domain) #adding domain to the container
for domain in websites_domains:
             print(domain)
"""==== end of block ===="""
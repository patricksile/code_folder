import MySQLdb
import time

#connecting to the mysql server
conn = MySQLdb.connect(host= "127.0.0.1",
              user="root",
              passwd="",
              db="scrapper")
#getting a cursor for the database
x = conn.cursor()

today = time.strftime("%Y-%m-%d")

x.execute("""SELECT * FROM houses""")
result = x.fetchall()
html_msg = """From: From Person <from@fromdomain.com>
                    To: To Person <to@todomain.com>
                    MIME-Version: 1.0
                    Content-type: text/html
                    Subject: Daily house updates : %s """ % (today)
for row in result:
    photo = row[0]
    id = row[1]
    date = row[2]
    title = row[3]
    description = row[4]
    price = row[5]
    town = row[6]
    domain = row[7]
    room = row[8]
    dimen = row[9]
    site = row[10]
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
print html_msg
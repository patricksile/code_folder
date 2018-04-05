from urllib.parse import urlparse

o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html/dsfasofsodfjoji4fdsa')
print(o.scheme + '://' + o.netloc[:-3])
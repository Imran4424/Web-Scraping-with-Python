from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")

bsobj = BeautifulSoup(html.read(),'lxml')

print(bsobj)
#print(bsobj.h1)
#print(bsobj.div)
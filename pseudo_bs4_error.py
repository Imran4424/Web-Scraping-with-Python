import scrapingtest
from bs4 import BeautifulSoup

bsobj = BeautifulSoup()

try:
    badContent = bsobj.nonExistingTag.anotherTag
except AttributeError as e:
    print("tag was not found")
else:
    if badContent == None:
        print("tag was not found")
    else:
        print(badContent)

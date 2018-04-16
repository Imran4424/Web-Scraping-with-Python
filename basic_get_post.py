import requests
import bs4

res1 = requests.get("https://en.wikipedia.org/wiki/List_of_districts_of_Bangladesh")

soup1 = bs4.BeautifulSoup(res1.content,"lxml")

for i, li in enumerate(lxml.select("li")):
    

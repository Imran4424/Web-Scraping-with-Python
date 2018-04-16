import requests
import bs4

url = "http://www.educationboardresults.gov.bd/"

res1 = requests.get(url)
soup1 = bs4.BeautifulSoup(res1.content, 'lxml')
x1 = soup1.find_all()
x1.attrs
x1['value']

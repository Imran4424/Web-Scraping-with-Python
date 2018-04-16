import requests
from bs4 import BeautifulSoup

session = requests.session();

url = "http://www.educationboardresults.gov.bd"

main_page = session.get(url)


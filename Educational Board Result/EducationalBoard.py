import requests
from bs4 import BeautifulSoup

session = requests.session();

url = "http://www.educationboardresults.gov.bd"

main_page = session.get(url)

form = BeautifulSoup(main_page.content,"lxml")

capcha = eval(form.form.table.table.find_all("tr")[6].find_all("td")[1].get_text())

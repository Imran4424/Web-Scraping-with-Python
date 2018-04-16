import requests
from bs4 import BeautifulSoup

session = requests.session()
form_page = session.get('http://www.educationboardresults.gov.bd')
form = BeautifulSoup(form_page.content, 'lxml')

captcha = eval(form.form.table.table.find_all('tr')
               [6].find_all('td')[1].get_text())
data = dict(sr=3, et=0, exam='ssc', year='2011', board="comilla",
            roll="166507", reg="871100", value_s=captcha)
result_page = session.post(
    'http://www.educationboardresults.gov.bd/result.php', data=data)
result = BeautifulSoup(result_page.content, 'lxml')
res = result.find('table', class_="black12").find_all('td')

information = {}
isKey = False
for item in res:
    if isKey:
        information[key] = item.get_text()
    else:
        key = item.get_text()
    isKey = not isKey

print(information)

import requests
from bs4 import BeautifulSoup

session = requests.session()

url = "http://www.educationboardresults.gov.bd"

main_page = session.get(url)

form = BeautifulSoup(main_page.content,"lxml")

capcha = eval(form.form.table.table.find_all("tr")[6].find_all("td")[1].get_text())


data = dict(sr=3,et=0,exam="ssc",year="2012",board = "dinajpur",roll="138272",reg = "750336",value_s = capcha)

result_url = "http://www.educationboardresults.gov.bd/result.php"

result_page = session.post(result_url,data = data)

result = BeautifulSoup(result_page.content,"lxml")

res = result.find("table",class_ = "black12").find_all("td")

information = {}

iskey = False

key = "0"

for item in res:
    if iskey:
        information[key] = item.get_text()
    else:
        key = item.get_text()
    iskey = not iskey

#print(information)

for keys in information:
    print(keys,information[keys])
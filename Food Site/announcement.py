import requests
from bs4 import BeautifulSoup

session = requests.session()

data = dict(user_name="admin", user_password="admin", user_login = "Log In")
page = session.post("http: // localhost/foodsite/index.php",data = data)

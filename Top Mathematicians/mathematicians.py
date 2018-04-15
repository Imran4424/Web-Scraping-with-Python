from requests import get
import bs4
from contextlib import closing

def is_good_response(resp):
    '''
    Return True if the response seems to be HTML, false otherwise
    '''

    content_type = resp.headers["content_type"].lower() 
    
    return (resp.status_code == 200 and content_type is not None and content_type.find("html"))


def simple_get(url):
    '''
    attempts to get the content at "url" by making a http request.
    if the content type response is some kind of HTML/XML, return the text context otherwise none 
    '''

    with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None



def get_names():
    '''
    downloads the the page where list of mathematicians is found and return a list of strings, one per mathematician
    '''

    url = "http://www.fabpedigree.com/james/mathmen.htm"

    response = simple_get(url)

    if response is not None:
        html = bs4.BeautifulSoup(response,"html.parser")

        names = set()

        for line in html.select("line"):
            for name in line.text.split("\n"):
                if len(name) > 0:
                    names.add(name.strip())
                            
        #return list(names)
        print(names)


get_names()

import request
import requests
import bs4


def simple_get(url):
    '''
    attempts to get the content at "url" by making a http request.
    if the content type response is some kind of HTML/XML, return the text context otherwise none 
    '''

    resp = requests.get(url,stream= True)

    if is_good_response(resp):
        return resp.content
    else:
        return None


def is_good_response(resp):
    
    
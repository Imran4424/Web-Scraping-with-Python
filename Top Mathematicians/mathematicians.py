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
    '''
    Return True if the response seems to be HTML, false otherwise
    '''

    content_type = resp.headers['Content_Type'].lower() 
    
    return (resp.status_code == 200 and content_type is not None and content_type.find('html'))

    
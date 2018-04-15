from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")

except HTTPError as e:
    print(e)
    # exception generated
except URLError as e:
    print("The server could not be found " + e)

else:
    print("It worked out well")
    #program continues
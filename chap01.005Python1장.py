from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPErrorBeautifulSoup as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e :
         return title

title = getTitle('http://github.com')
if title == None:
    print('Title could not be found')
else:
    print(title)

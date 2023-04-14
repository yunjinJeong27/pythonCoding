from urllib.request import urlopen 
from bs4 import BeautifulSoup 
import datetime 
import random 
import re 

random.seed(datetime.datetime.now()) 

def getLinks(githubUrl): 
html = urlopen('http://en.wikipedia.org{}'.format(githubUrl)) 

bs = BeautifulSoup(html,'html.parser') 
return bs.find('div', {'id':'bodyContent'}).find_all('a',
href=re.compile('^(/wiki/)((?!:).)*$')) 

links = getLinks('/wiki/github') 
while len(links) > 0: 
newPage = links[random.randint(0, len(links)-1)].attrs['href'] 
print(newPage) 
links = getLinks(newPage)

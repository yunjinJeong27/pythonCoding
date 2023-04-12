from urllib.request import urlopen 
from bs4 import BeautifulSoup 
import re 

html = urlopen('http://www.github’) 
bs = BeautifulSoup(html, 'html.parser’) 
images = bs.find_all('img', {'src':re.compile('\/img\/gifts/img.*\.jpg')}) 
for image in images: 
print(image['src'])

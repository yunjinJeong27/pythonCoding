from urllib.request import urlopen 
from bs4 import BeautifulSoup 

html = urlopen(“http://www.github”) 
bs = BeautifulSoup(html, "html.parser")


titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6’]) 
print([title for title in titles])


allText = bs.find_all('span', {'class':{'green', 'red'}}) 
print([text for text in allText])


nameList = bs.find_all(text='box) 
print(len(nameList))


title = bs.find_all(id='title', class_='text’) 
print([text for text in allText])

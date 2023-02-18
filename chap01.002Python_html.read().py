from urllib.request import urlopen
html = urlopen('http://github.com')
print
print(html.read())

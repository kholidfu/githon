import urllib2
from bs4 import BeautifulSoup
import time

url = "http://www.vectorfreak.com"
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

html = opener.open(url).read()
soup = BeautifulSoup(html)

# begin parsing
div = soup.find('div', attrs={'class': 'index_tags'})
div = div.find('div', attrs={'class': 'tags_box'})
ahrefs = div.findAll('a')

freaktags = [i.getText() for i in ahrefs]

with open('/home/banteng/gitcode/githon/vectormetags.txt') as f:
    tags = f.readlines()
    tags = [tag.strip() for tag in tags]

with open('/home/banteng/gitcode/githon/vectormetags.txt', 'a') as f2:    
    for i in freaktags:
        if i not in tags:
            f2.write(i + '\n')

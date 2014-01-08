import urllib2
from bs4 import BeautifulSoup

url = "http://vector.me/tags/"
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
html = opener.open(url + "1")
soup = BeautifulSoup(html)

tags = soup.find('div', attrs={'class': 'tags_cloud'})
tags = tags.findAll('a')

with open('/home/banteng/Desktop/vectormetags.txt', 'wa') as f:
    for tag in tags:
        f.write(tag.getText() + '\n')

import urllib2
from bs4 import BeautifulSoup
import time

url = "http://vector.me/tags/"
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

with open('/home/banteng/Desktop/vectormetags.txt', 'wa') as f:
    for i in range(1, 101):
        print "Starting %s" % url + str(i)
        html = opener.open(url + str(i))
        soup = BeautifulSoup(html)
        tags = soup.find('div', attrs={'class': 'tags_cloud'})
        tags = tags.findAll('a')

        for tag in tags:
            f.write(tag.getText() + '\n')

        time.sleep(3)
        print "wait for 3 second"

#!/usr/bin/python
# author: @sopier
# created: July 2012

""" This little program lets you download Youtube video just by giving
the Youtube URL.

At first, this program will try to look for the MP4 video format 
with highest resolution, if it's not found, it will search for whatever
available video format with the highest resolution (webm or flv). 

It also has simple progress bar which will let you know the download 
progress so far.

=========

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""


import urllib
import re
import sys


def progress(count, blocksize, totalsize):
    percent = int(count * blocksize * 100 / totalsize)
    sofar = count * blocksize
    sys.stdout.write("\r" + "%d%%... %d completed from %d" % (percent, sofar, totalsize))
    sys.stdout.flush()


def grab_youtube(url):
    url = sys.argv[1]
    # @TODO: kalau passing url dengan tanda &, linux membacanya sebagai background jobs :(
    raw_url = 'http://www.youtube.com/watch?' + re.search(re.compile(r"v[\w=-]+"), url).group()
    page = urllib.urlopen(raw_url).read()
    page = urllib.unquote_plus(page)
    page = urllib.unquote(page)
    try:
        url_match = re.search(re.compile(r"(http://o-o---.*&quality=.*&type=video/mp4)"), page).group(1)
        url_to_download = url_match.split('url=') # get the first match (highest resolution)
        url_to_download = [i for i in url_to_download if 'mp4' in i][0]
        url_to_download = url_to_download.split('="')[0]
    except:
        url_match = re.search(re.compile(r"(http://o-o---.*&quality=.*&type=video/x-flv)"), page).group(1)
        url_to_download = url_match.split('url=')[0] # get the first match (highest resolution)
        url_to_download = url_match.split(';')[0] # get the first match (highest resolution)
        url_to_download = url_to_download.split('="')[0]

    print ''
    print 'Download started... Please wait...'

    title = re.search(re.compile(r"<title>(.*)- YouTube", re.DOTALL), page).group(1).replace('\n', ' ').strip()

    try:
        filename = title.lower().replace(' ', '_')  # advanced_python_or_understanding_python
    except:
        # catch the unix reserved characters for filename (/:><|&) n get rid of them
        filename = title.lower().replace('/', ' ').replace(':', ' ').replace('>', ' ').replace('<', ' ').replace('|', ' ').replace('&', ' ').replace(' ', '_')

    # get file extension
    file_ext = urllib.urlopen(url_to_download).info().getheaders("Content-Type")[0].split("/")[1]
    
    # processing the download
    urllib.urlretrieve(url_to_download, filename + '.' + file_ext, progress)
    
    print
    print 'Download finished'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print """Usage: python main.py <url youtube> """
        print """ex: python main.py http://www.youtube.com/watch?v=E_kZDvwofHY """
    else:
        grab_youtube(sys.argv[1])

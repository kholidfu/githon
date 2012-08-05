#!/usr/bin/python
# @TODO: handle error: file not found?
# for temporary reason I use simple exception to handle that

import os

folder = os.path.realpath(os.path.dirname(__file__))

folder_size = 0

for (path, dirs, files) in os.walk(folder):
    for f in files:
        filename = os.path.join(path, f)
        try:
            folder_size += os.path.getsize(filename)
        except:
            continue

print "Ukuran Folder %s => %.1f MB" % (folder.split('/')[-1], 
        folder_size / (1024*1024.0))

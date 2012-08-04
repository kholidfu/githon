#!/usr/bin/python

"""
"""

# how to filter non-letter characters?

def word_counter(fromfile):
    words = {}
    f = open(fromfile, 'r')

    for i in f.readlines():
        for j in i.split():
            if j in words:
                num = words.get(j)
                words.update({j: num+1})
            else:
                words.update({j: 1})

    f.close()

    for i in sorted(words, key=words.get, reverse=True):
        print i, ':', words[i]

if __name__ == '__main__':
    word_counter('somefile.txt')
    print '*' * 40
    word_counter('youtube_downloader.py')

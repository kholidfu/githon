#!/usr/bin/python
# Kholid Fuadi
# @sopier
# Tue Aug  7 00:15:29 WIT 2012

"""Simple module to cut long line ( >n characters)"""

def line_cutter(line, num):
    
    n = len(line) / num
    newline = []
    breaker_lama = 0
    for i in range(1, n+1):
        breaker = line[:num*i].rfind(' ')
        newline.append(line[breaker_lama:breaker] + '\n')
        breaker_lama = breaker + 1
    newline.append(line[breaker_lama:] + '\n')

    newline = ''.join(newline)
    return newline



if __name__ == '__main__':
    # open new file
    # newfile = open('/tmp/dummy.txt', 'w')

    # save it to newfile
    #with open('/home/banthink/Dropbox/kuliah/latex_lat/tesis-latex/tesis_latex.tex') as f:
    #    for line in f:
    #        if len(line) > 79:
    #            newfile.write(line_cutter(line, 70))
    #        else:
    #            newfile.write(line)

    longline = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
    print line_cutter(longline, 50)

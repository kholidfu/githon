#!/usr/bin/python
#@sopier
#Wed Aug  8 13:23:37 WIT 2012


"""Explaining the concept of iterator (using builtin iter func)"""


iter_obj = iter('sopier')

while True:
    try:
        print iter_obj.next()
    except StopIteration:
        break

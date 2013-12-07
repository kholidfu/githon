#!/usr/bin/python

def make_bold(fn):
    def inner():
        return '<b>' + fn() + '</b>'
    return inner

@make_bold
def kata():
    """It must return like this:
    >>> '<b>ahnaf</b>'"""
    return 'ahnaf'

print kata()

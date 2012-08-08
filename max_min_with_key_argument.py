#!/usr/bin/python
#@sopier
#Wed Aug  8 13:30:49 WIT 2012

"""Here is an example usage of max/min function with optional 
key argument."""

# regular max usage
print max(2, 3, -4)

# now let's add the key argument
print max(2, 3, -4, key=abs)

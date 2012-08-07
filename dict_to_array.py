#!/usr/bin/python
# @sopier
# Tue Aug  7 21:49:52 WIT 2012

"""Here is how to convert Python dict type object
into PHP array"""

import json

d = {}
d{'name': 'sopier'}

with open('/tmp/mydict.json', mode='w') as f:
    json.dump(d, f)

# using PHP using you can decode using json_decode
# function
# $data = json_decode(file_get_contents('/tmp/mydict.json'));
# var_dump($data);

#!/usr/bin/python

import datetime

timestamp = 1478347216
print(
    datetime.datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y')
)
 

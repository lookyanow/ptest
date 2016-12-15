#!/usr/bin/python

import sqlite3

from db import *

conn = DBLite("films.db")
for row in conn.query("select * from films"):
	print row

for i in conn.query("select * from films order by view_date desc"):
	print i['title']
	print i['info_link']

films = []
for i in conn.query("select * from films order by view_date desc"):
	films.append(i)

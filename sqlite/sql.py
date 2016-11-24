#!/usr/bin/python

import sqlite3

con = sqlite3.connect('test.db')
con.row_factory = sqlite3.Row
cur = con.cursor()
cur.execute('SELECT *FROM users')
res = cur.fetchall()
con.close()


for i in res:
	print i['id']
	print i['firstName']

#!/usr/bin/python

import urllib2

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup


try:
	html= urlopen("http://rutor.is/top")
except urllib2.HTTPError as e:
	print e
else:
	try:
		bsobj = BeautifulSoup(html.read())
	except AttributeError as e:
		print e
	
	print bsobj.title
	films = bsobj.findAll("tr", {"class":"tum"})
	for film in films:
		print film

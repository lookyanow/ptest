#!/usr/bin/python 

class Test:
	a = 0
	b = 0 
	string = ""
	def __init__(self):
		print "Constructor of Test class"
	def say_hello(self, string):
		print string

class NewTest(Test):
	a = 0
	b = 0 
	string = ""
	def __init__(self):
		print "Constructor of NewTest class"
	def say_hello(self, string):
		print "%s from NewTest Class" % string


obj1 = Test()
obj2 = NewTest()

obj1.say_hello("Hello")
obj2.say_hello("Hello")

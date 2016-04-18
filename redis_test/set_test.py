#!/usr/bin/python

import redis;

r = redis.StrictRedis(host='redis01d.dst.yandex.net', port='6379', db=0)

for num in range(1,100000):
	s = "user:%d" % (num)
	print r.set(s,num)


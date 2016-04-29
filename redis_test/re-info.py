#!/usr/bin/python

import redis;

r = redis.StrictRedis(host='redis01d.dst.yandex.net', port='6379', db=0)
data=r.info()

print data['role']
print data['connected_slaves']
print data['slave0']['state']
print data['slave0']['lag']


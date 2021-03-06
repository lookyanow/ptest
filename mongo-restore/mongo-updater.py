#!/usr/bin/python 

import subprocess
import datetime
import shlex

from bson.objectid import ObjectId
from pymongo import MongoClient

def mongodump(mongohost,db,collection,object_id):
    """Makes mongo database dump by mongodump"""
    
    print object_id
    command_args = """mongodump --host %s:27017 --db %s --collection %s --username ics --password "2Jl2tG7i" --query '{_id: {$gt: ObjectId("%s")}}' --out /var/lib/mongodb/dump/""" % (mongohost,db,collection,object_id)
    print command_args
    command = shlex.split(command_args)
    p = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    out, err = p.communicate()
    print out
    print err
    return p.returncode

def mongorestore(mongohost='localhost'):
    """Restores mongodb dump to localhost"""
    
    command_args = """mongorestore --host %s:27017 --username admin --password "I2CqWek" /var/lib/mongodb/dump/""" % (mongohost)
    print command_args
    command = shlex.split(command_args)
    p = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    out, err = p.communicate()
    print out
    print err
    return p.returncode

def collectionlist(mongohost,db,user='',password=''):
    """Get collections list"""
   
    uri = "mongodb://%s:%s@localhost/ics" % (user,password)
   
    conn = MongoClient(uri)

    db = conn['ics']
    collection = db.collection_names(include_system_collections=False)
    return collection

def removealldocs(mongohost='localhost'):
    """Removing all document from collection"""

    uri = "mongodb://ics:2Jl2tG7i@localhost/ics"
    conn = MongoClient(uri)

    db = conn['ics']
    colls = collectionlist('localhost','ics','ics','2Jl2tG7i')
    for coll in colls:
        c = db[coll]
        result = c.delete_many({})
	deletestr = "%d documents deleted from %s collection " % (result.deleted_count,coll)
        print deletestr


def getobjectid(days_ago):
    """Returns Mongodb Objectid than was some days in the past"""
    now_date = datetime.datetime.today()
    now_date = now_date.replace(hour=0, minute=0, second=0, microsecond=0)
    gen_time = now_date - datetime.timedelta(days=days_ago) 
    dummy_id = ObjectId.from_datetime(gen_time)
    return dummy_id

#collection = collectionlist("localhost")

#for collect in collection:
#    print collect

dump_id = getobjectid(30)

# 1. Get dump 
# 2. Remove all local documents
# 3. Restore data

colls = collectionlist('localhost','ics','ics','2Jl2tG7i')

for coll in colls:
    result = mongodump('ics-dct-prod-mongo-node1.ru.mgo.su','ics',coll,dump_id)

if result ==0:
    removealldocs('localhost') #VERY carefull with hostname
    mongorestore()
else:
    print "Error during mongodump"

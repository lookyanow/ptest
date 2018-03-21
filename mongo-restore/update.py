#!/usr/bin/python 

import subprocess
import datetime
import shlex

from bson.objectid import ObjectId
from pymongo import MongoClient

def mongodump(mongohost,db,collection,object_id):
    """Makes mongo database dump by mongodump"""
    
    print object_id
    command_args = """mongodump --host %s:27017 --db %s --collection %s --username ics --password "2Jl2tG7i" --query '{_id: {$gt: ObjectId("%s")}}' --out dump/""" % (mongohost,db,collection,object_id)
    print command_args
    command = shlex.split(command_args)
    p = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    out, err = p.communicate()
    print out
    print err
    print p.returncode

def mongorestore(mongohost='localhost'):
    """Restores mongodb dump to localhost"""
    
    command_args = """mongorestore --host %s:27017 dump/""" % (mongohost)
    print command_args
    command = shlex.split(command_args)
    p = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    out, err = p.communicate()
    print out
    print err
    print p.returncode

def collectionlist(mongohost):
    """Get collections list"""
    
    conn = MongoClient(mongohost,27017)

    db = conn['ics']
    collection = db.collection_names(include_system_collections=False)
    return collection

def removealldocs(mongohost='localhost'):
    """Removing all document from collection"""
    conn = MongoClient(mongohost,27017)

    db = conn['ics']
    colls = collectionlist('localhost')
    for coll in colls:
        c = db[coll]
        c.delete_many({})

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

dump_id = getobjectid(1)

removealldocs('localhost') #VERY carefull with hostname 

mongodump('ics-dct-prod-mongo-node1.ru.mgo.su','ics','events',dump_id)

mongorestore()



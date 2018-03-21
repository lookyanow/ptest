#!/usr/bin/python 

import subprocess
import datetime

from bson.objectid import ObjectId
from pymongo import MongoClient

def mongodump(mongohost,db,object_id):
    """Makes mongo database dump by mongodump"""
    
    command_args = """--host %s:27017 --db %s --username ics --password "2Jl2tG7i" --query '{_id: {$gt: ObjectId("%s")}}' --out dump/""" % (mongohost,db,object_id)
    p = subprocess.Popen(['mongodump',command_args],shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    out, err = p.communicate()
    print out
    print err


def collectionlist(mongohost):
    """Get collections list"""
    
    conn = MongoClient(mongohost,27017)

    db = conn['ics']
    collection = db.collection_names(include_system_collections=False)
    return collection

def getobjectid(days_ago):
    """Returns Mongodb Objectid than was some days in the past"""
    now_date = datetime.datetime.today()
    now_date = now_date.replace(hour=0, minute=0, second=0, microsecond=0)
    gen_time = now_date - datetime.timedelta(days=days_ago) 
    dummy_id = ObjectId.from_datetime(gen_time)
    return dummy_id

collection = collectionlist("localhost")

#for collect in collection:
#    print collect

#mongodump('ics-dct-prod-mongo-node1.ru.mgo.su','ics','5a854c100000000000000000')

print getobjectid(1)
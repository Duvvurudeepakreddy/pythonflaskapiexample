import os
import pandas as pd
import time
import psycopg2
import datetime
import json
import logging

hostname="localhost"
databasename="postgres"
username="postgres"
password="root"
portname="5432"
dtfile = datetime.datetime.now()

logger = logging.getLogger('loggingerror')
logger.setLevel(logging.WARNING)
logfilename = "project"+".log"
ch = logging.FileHandler(filename=logfilename)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def insertintotable(d):
    try:

        colnames = ""
        valueslist = []
        samplestr = "("
        for key in d.keys():
            colnames = colnames + key + ","
            valueslist.append(d[key])
            samplestr = samplestr + "%s,"

        samplestr = samplestr[:-1]
        samplestr = samplestr + ")"
        colnames = colnames[:-1]
        conn = psycopg2.connect(dbname=databasename, user=username, host=hostname, password=password, port=portname)
        sql = "insert into tabledata.songsdata(" + colnames + ") VALUES " + samplestr
        # print("sql=",sql)
        cursor = conn.cursor()
        cursor.execute(sql, tuple(valueslist))
        conn.commit()
        cursor.close()
        conn.close()
        print("inserted successfullly")
        return "success"
    except (Exception) as e:
        logger.exception(e)
        print(e)


def deletefromtable(id):
    try:
        print(id)
        conn = psycopg2.connect(dbname=databasename, user=username, host=hostname, password=password, port=portname)
        sql = "delete from tabledata.songsdata where id="+id
        # print("sql=",sql)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        print("deleted successfullly")
        return "success"
    except (Exception) as e:
        logger.exception(e)
        print(e)

def selectdatabytypeandid(type,id):
    try:
        print(id)
        conn = psycopg2.connect(dbname=databasename, user=username, host=hostname, password=password, port=portname)
        sql = "select * from tabledata.songsdata where type='"+type+"' and id="+id
        # print("sql=",sql)
        data=pd.read_sql(sql,conn)
        finallist=data.to_dict(orient='records')
        print(finallist)
        conn.close()
        return finallist
    except (Exception) as e:
        logger.exception(e)
        print(e)



def selectdatabytype(type):
    try:
        print(type)
        conn = psycopg2.connect(dbname=databasename, user=username, host=hostname, password=password, port=portname)
        sql = "select * from tabledata.songsdata where type='"+type+"'"
        # print("sql=",sql)
        data=pd.read_sql(sql,conn)
        finallist=data.to_dict(orient='records')
        print(finallist)
        conn.close()
        return finallist
    except (Exception) as e:
        logger.exception(e)
        print(e)

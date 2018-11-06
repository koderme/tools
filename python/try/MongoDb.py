#!/usr/bin/python3.6

import os
import unittest
import sys

import pymongo
from pymongo import MongoClient

def getDbNames():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	return myclient.list_database_names()

def authenticate():

	authMech = 'SCRAM-SHA-256'
	authMech = 'SCRAM-SHA-1'  ### This works

	client = MongoClient('mongodb://localhost:27017/',
		username='vishal',
		password='vishal',
		authSource='ecomm',
		authMechanism=authMech)

	print("---------------------")
	print("dbclient:" + str(client))

	return client

def getCollections(dbClient, dbName):
	myDb = dbClient[dbName]
	print("---------------------")
	collArr = myDb.list_collection_names()
	print("collArr:" + str(collArr))

def getCollection(dbClient, dbName, collName):
	myDb = dbClient[dbName]
	myCol = myDb[collName]
	print("---------------------")
	print("myCol:" + str(myCol))

#------------------------------------------
# Unit test
#------------------------------------------
class TestMyClass(unittest.TestCase):


	def test_1(self):
		dbClient = authenticate()
		getCollections(dbClient, "ecomm")



# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
unittest.TextTestRunner(verbosity=2).run(suite)

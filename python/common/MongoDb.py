#!/usr/bin/python3.6

import os
import unittest
import sys
sys.path.append('..')
import logging

import pymongo
from pymongo import MongoClient

from common.Utils import *

#logging.basicConfig(filename='try.log',level=logging.DEBUG)
logging.basicConfig(filename='try.log',level=logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setLevel(logging.INFO)
logger = logging.getLogger('try')
logger.addHandler(ch)

# Defaults for testing
newLine = "\n"
collName = "emp1"
dbName = "ecomm"
authMech = 'SCRAM-SHA-256'
authMech = 'SCRAM-SHA-1'  ### This works

class MongoDb:
	def __init__(self, connString, loginId, password, authSource):
		self.connString = connString
		self.loginId = loginId
		self.password = password
		self.authSource = authSource

	def authenticate(self):

		dbClient = MongoClient(self.connString,
			username=self.loginId,
			password=self.password,
			authSource=self.authSource,
			authMechanism=authMech)

		self.dbClient = dbClient
		logger.debug("authenticate:" + str(dbClient))

	def authenticate2(self):
		authMech = 'SCRAM-SHA-256'
		authMech = 'SCRAM-SHA-1'  ### This works

		dbClient = MongoClient('mongodb://localhost:27017/',
			username='vishal',
			password='vishal',
			authSource='ecomm',
			authMechanism=authMech)

		self.dbClient = dbClient
		logger.debug("authenticate:" + str(dbClient))

	def getColl(self, dbName, collName):
		myDb = self.dbClient[dbName]
		return myDb[collName]

	def getDbNames(self):
		return self.dbClient.list_database_names()

	def getCollections(self, dbName):
		myDb = self.dbClient[dbName]
		return myDb.list_collection_names()

	# Delete methods
	def deleteOne(self, dbName, collName, query):
		#myquery = { "address": "Mountain 21" }
		self.getColl(dbName, collName).delete_one(query)

	def deleteMany(self, dbName, collName, query):
		#myquery = { "address": {"$regex": "^S"} }
		self.getColl(dbName, collName).delete_many(query)

	def deleteAll(self, dbName, collName):
		self.getColl(dbName, collName).delete_many({})

	# Insert
	def insertOne(self, dbName, collName, doc):
		result = self.getColl(dbName, collName).insert_one(doc)

	def insertMany(self, dbName, collName, docArr):
		result = self.getColl(dbName, collName).insert_many(docArr)

	# Find methods
	def find_allDocs_allFields(self, dbName, collName):
		return self.getColl(dbName, collName).find({})

	def find_allDocs_selectedFields(self, dbName, collName, selectFieldDict):
		# { "_id": 0, "name": 1, "address": 1 }
		return self.getColl(dbName, collName).find({}, selectFieldDict)

	def find_allDocs_allFields_sorted(self, dbName, collName, sortOrder):
		return self.getColl(dbName, collName).find({}).sort(sortOrder)

	# Search
	def find(self, dbName, collName, query):
		#query = { "empno": "10" }

		# Note that find return object of type Cursor
		return self.getColl(dbName, collName).find(query)

#------------------------------------------
# Unit test
#------------------------------------------
class TestMyClass(unittest.TestCase):

	connString = 'mongodb://localhost:27017/'
	mdb = MongoDb(connString, "vishal", "vishal", "ecomm")

	def show(result):
		for doc in result:
			logger.debug(" doc: " + str(doc))

	def insert_10_11_12(self):
		# Insert
		docs =  [
					{ "empno": 11, "name": "John", "salary":10000 },
					{ "empno": 12, "name": "Aby", "salary":5000 },
					{ "empno": 13, "name": "Zucker", "salary":20000 },
					{ "empno": 14, "name": "Albert", "salary":20000 },
				]
		self.mdb.insertMany(dbName, collName, docs)


	def test_auth(self):
		TestMyClass.mdb.authenticate()

	def test_find(self):
		empno = Utils.currentTimestamp()
		self.mdb.deleteAll(dbName, collName)

		# Insert
		doc = { "empno": empno }
		self.mdb.insertOne(dbName, collName, doc)

		query = doc
		result = self.mdb.find(dbName, collName, query)
		self.assertNotEqual(None, result[0])
		self.assertEqual(empno, result[0]['empno'])

	def test_deleteOne(self):
		self.mdb.deleteAll(dbName, collName)
		empno = Utils.currentTimestamp()

		# Insert
		doc = { "empno": empno }

		# delete
		query = { "empno": empno }
		self.mdb.deleteOne(dbName, collName, query)

		# Confirm that they don't exist
		result = self.mdb.find(dbName, collName, query)
		self.assertEqual(0, result.count())

	def test_deleteMany(self):

		self.insert_10_11_12()

		# delete
		query = { "empno": 10 }
		self.mdb.deleteMany(dbName, collName, query)

		# Confirm that they don't exist
		result = self.mdb.find(dbName, collName, query)
		self.assertEqual(0, result.count())
		
	def test_find_allDocs_allFields(self):
		self.mdb.deleteAll(dbName, collName)
		self.insert_10_11_12()
		result = self.mdb.find_allDocs_allFields(dbName, collName)
		self.assertEqual(4, result.count())
		self.assertNotEqual(None, result[0]['empno'])

	def test_find_allDocs_allFields_sorted(self):
		self.mdb.deleteAll(dbName, collName)
		self.insert_10_11_12()
		sortOrder = [
        		('salary', pymongo.DESCENDING),
        		('name', pymongo.ASCENDING),
			]
		result = self.mdb.find_allDocs_allFields_sorted(dbName, collName, sortOrder)
		self.assertEqual(4, result.count())
		self.assertEqual(14, result[0]['empno'])

	def test_find_allDocs_selectedFields(self):
		self.mdb.deleteAll(dbName, collName)
		self.insert_10_11_12()

		selectFieldDict = { "_id":0, "empno":1 }
		result = self.mdb.find_allDocs_selectedFields(dbName, collName, selectFieldDict)
		self.assertEqual(4, result.count())

	def test_insert_rec(self):

		self.mdb.deleteAll(dbName, collName)
		for x in range(1000):
			self.insert_10_11_12()

		result = self.mdb.find_allDocs_allFields(dbName, collName)
		self.assertEqual(4000, result.count())

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
unittest.TextTestRunner(verbosity=2).run(suite)

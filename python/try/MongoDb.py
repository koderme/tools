#!/usr/bin/python3.6

import os
import unittest
import sys

import pymongo
from pymongo import MongoClient

def getDbNames():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	return myclient.list_database_names()

#------------------------------------------
# Unit test
#------------------------------------------
class TestMyClass(unittest.TestCase):

	def authenticate(self):

		client = MongoClient('mongodb://localhost:27017/',
			username='user',
			password='password',
			authSource='the_database',
			authMechanism='SCRAM-SHA-256')

	def test_search(self):
		dbnameList = getDbNames()
		print('db names: ' + str(dbnameList))	



# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
unittest.TextTestRunner(verbosity=2).run(suite)

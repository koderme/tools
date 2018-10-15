#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from Common import *
from model.ReferenceData import *


#-------------------------------------------------------------
# CvParseResult is a dictionary of
#    section-name Vs <attribute-dict>
#    The <attribute-dict> stored dict of 
#     <attrKey> Vs <attrValue>
#-------------------------------------------------------------
class CvParseResult:
	def __init__(self):
		self.contentDict = {}

	def add(self, sectionName, attrKey, attrValue):
		attrDict = self.contentDict.get(sectionName)
		if (attrDict == None):
			attrDict = {}
			self.contentDict[sectionName] = attrDict
		attrDict[attrKey] = attrValue

	def getAttrValue(self, sectionName, attrKey):
		attrDict = self.contentDict.get(sectionName)
		if (attrDict == None):
			return None

		return attrDict.get(attrKey, None)

	def getSectionDict(self, sectionName):
		attrDict = self.contentDict.get(sectionName)
		if (attrDict == None):
			attrDict = {}
			self.contentDict[sectionName] = attrDict
		return attrDict

	def __str__(self):
		retStr = ''
		for secName, attrDict in self.contentDict.items():
			retStr += '\n[' + secName + '] ==> '  + str(attrDict)

		return retStr


#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestCvParseResult(unittest.TestCase):

	def test_get_attr(self):

		pr = CvParseResult()

		pr.add(Ref.Section.personal.name, 'name', 'John White')
		pr.add(Ref.Section.personal.name, 'emailid', 'test@gmail.com')

		attrValue = pr.getAttrValue(Ref.Section.personal.name, 'name')
		self.assertEqual('John White', attrValue)

		attrValue = pr.getAttrValue(Ref.Section.personal.name, 'emailid')
		self.assertEqual('test@gmail.com', attrValue)

		# Unknown section
		attrValue = pr.getAttrValue(Ref.Section.unknown.name, 'name')
		self.assertEqual(None, attrValue)

		# Unknown attr
		attrValue = pr.getAttrValue(Ref.Section.personal.name, '--invalid--')
		self.assertEqual(None, attrValue)


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
logging.basicConfig(level=logging.INFO)
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvParseResult)
unittest.TextTestRunner(verbosity=2).run(suite)

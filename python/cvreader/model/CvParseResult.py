#!/usr/bin/python3.6

import os
import unittest
import json
import sys

sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from model.ReferenceData import *

logger = logging.getLogger('cvreader')

#-------------------------------------------------------------
# CvParseResult is a dictionary of
#    section-name Vs <attribute-dict>
#    The <attribute-dict> stored dict of 
#     <attrKey> Vs <attrValue>
#-------------------------------------------------------------
class CvParseResult:
	def __init__(self):
		self.secDict = {}

	def add(self, sectionName, attrKey, attrValue):
		secAttrDict = self.secDict.get(sectionName)
		if (secAttrDict == None):
			secAttrDict = {}
			self.secDict[sectionName] = secAttrDict
		secAttrDict[attrKey] = attrValue

	def getAttrValue(self, sectionName, attrKey):
		secAttrDict = self.secDict.get(sectionName)
		if (secAttrDict == None):
			return None

		return secAttrDict.get(attrKey, None)

	def getSectionDict(self, sectionName):
		secAttrDict = self.secDict.get(sectionName)
		if (secAttrDict == None):
			secAttrDict = {}
			self.secDict[sectionName] = secAttrDict
		return secAttrDict

	def getSecDict(self):
		return self.secDict

	def getSecDictAsJson(self):
		return json.dumps(self.secDict, indent=2)

	def __str__(self):
		retStr = ''
		for secName, secAttrDict in self.secDict.items():
			retStr += '\n[' + secName + '] ==> '  + str(secAttrDict)

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
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvParseResult)
unittest.TextTestRunner(verbosity=2).run(suite)

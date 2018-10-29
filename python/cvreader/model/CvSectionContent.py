#!/usr/bin/python3.6

import os
import unittest
import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from model.ReferenceData import *

logger = logging.getLogger('cvreader')

#-------------------------------------------------------------
#-------------------------------------------------------------
class CvSectionContent:
	def __init__(self, secName):
		self.secName = secName
		self.lineList = []

	def addLine(self, line):
		self.lineList.append(line)

	def getSecName(self):
		return self.secName	

	def getLineList(self):
		return self.lineList	

	def __str__(self):
		retStr = '\n---------------' + self.secName + '---------------'
		for line in self.lineList:
			retStr += '\n' + line
		return retStr
#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestThisClass(unittest.TestCase):

	def test_get_addline(self):

		obj = CvSectionContent('sec1')

		obj.addLine('email: test@gmail.com')
		obj.addLine('name: John White')

		self.assertEqual('sec1', obj.getSecName())

		lineList = obj.getLineList()
		self.assertEqual(2, len(lineList))


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestThisClass)
unittest.TextTestRunner(verbosity=2).run(suite)

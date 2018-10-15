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
# CvContent is a dictionary of
#    section-name Vs lineList[]
#-------------------------------------------------------------
class CvContent:
	def __init__(self):
		self.contentDict = {}

	def addLine(self, sectionName, line):
		lineList = self.contentDict.get(sectionName)
		if (lineList == None):
			lineList = []
			self.contentDict[sectionName] = lineList
		lineList.append(line)

	def getLineList(self, sectionName):
		lineList = self.contentDict.get(sectionName)
		if (lineList == None):
			return []
		return lineList	

	def getContentDict(self):
		return self.contentDict

	def __str__(self):
		retStr = ''
		for secName,lineList in self.contentDict.items():
			retStr += '\n---------------' + secName + '---------------'
			for line in lineList:
				retStr += '\n' + line
		return retStr
#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestCvContent(unittest.TestCase):

	def test_get_sentence(self):

		content = CvContent()

		content.addLine(Ref.Section.personal.name, 'email: test@gmail.com')
		content.addLine(Ref.Section.personal.name, 'name: John White')

		lineList = content.getLineList(Ref.Section.personal.name)
		self.assertEqual(2, len(lineList))

		content.addLine(Ref.Section.skill.name, 'java cpp python')
		lineList = content.getLineList(Ref.Section.skill.name)
		self.assertEqual(1, len(lineList))

		lineList = content.getLineList(Ref.Section.unknown.name)
		self.assertEqual(0, len(lineList))



# Run unit tests
#if __name__ == '__main__':
#unittest.main()
logging.basicConfig(level=logging.INFO)
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvContent)
unittest.TextTestRunner(verbosity=2).run(suite)

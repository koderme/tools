#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from model.ReferenceData import *
from model.CvSectionContent import *

logger = logging.getLogger('cvreader')

#-------------------------------------------------------------
# CvContent is list of CvSectionContent
#-------------------------------------------------------------
class CvContent:
	def __init__(self):
		self.secContentList = []
		self.curSecContent = None

	def addLine(self, secName, line):

		if ((self.curSecContent == None) or
			(self.curSecContent.getSecName() != secName)):
			self.curSecContent = CvSectionContent(secName)
			self.secContentList.append(self.curSecContent)

		self.curSecContent.addLine(line)

	def getSecContent(self, secName):
		for secContent in self.secContentList:
			if secContent.getSecName() == secName:
				return secContent
		return None

	def getSecContentList(self):
		return self.secContentList

	def size(self):
		return len(self.secContentList)

	def __str__(self):
		retStr = ''
		for secContent in self.secContentList:
			retStr += str(secContent)
		return retStr
#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestThisClass(unittest.TestCase):

	def test_get_sentence(self):

		obj = CvContent()

		obj.addLine(Ref.Section.personal.name, 'email: test@gmail.com')
		obj.addLine(Ref.Section.personal.name, 'name: John White')

		obj.addLine(Ref.Section.skill.name, 'java cpp python')
		obj.addLine(Ref.Section.skill.name, 'unix ml')

		self.assertEqual(2, obj.size())
		self.assertEqual(Ref.Section.personal.name, obj.getSecContent(Ref.Section.personal.name).getSecName())
		self.assertEqual(Ref.Section.skill.name, obj.getSecContent(Ref.Section.skill.name).getSecName())


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestThisClass)
unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/python3.6

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

	def addLine(self, secName, line, startNewSection=False):

		# Its a new section when:
		#  [1] Current section is None
		#  [2] startNewSection is True
		#  [3] specified secName is different that curr secName
		if ((self.curSecContent == None) or
			(startNewSection) or 
			(self.curSecContent.getSecName() != secName)):
			self.curSecContent = CvSectionContent(secName)
			self.secContentList.append(self.curSecContent)

		self.curSecContent.addLine(line)

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

	def test_get_addLine(self):

		obj = CvContent()

		obj.addLine(Ref.Section.personal.name, 'email: test@gmail.com')
		obj.addLine(Ref.Section.personal.name, 'name: John White')

		obj.addLine(Ref.Section.skill.name, 'java cpp python')
		obj.addLine(Ref.Section.skill.name, 'unix ml')

		self.assertEqual(2, obj.size())

	def test_get_addLine_newsection(self):

		obj = CvContent()

		obj.addLine(Ref.Section.personal.name, 'email: test@gmail.com')
		obj.addLine(Ref.Section.personal.name, 'name: John White')

		startNewSection = True	
		obj.addLine(Ref.Section.skill.name, 'java cpp python', startNewSection)
		obj.addLine(Ref.Section.skill.name, 'unix ml')

		obj.addLine(Ref.Section.skill.name, 'bigdata kafka', startNewSection)
		obj.addLine(Ref.Section.skill.name, 'spark')

		self.assertEqual(3, obj.size())

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestThisClass)
unittest.TextTestRunner(verbosity=2).run(suite)

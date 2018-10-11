#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')

from common.Utils import *


CvTag =  Enum('', 'summary skill role project employer certification personal')
NewLine = '\n'

#---------------------------------------------------
# CvSection represents 1 section of Cv.
# It stores following metadata
#    secName
#         -- name of the section
#    secTags  
#         -- they are used to identify start of section.
#         -- if line is identified as <SectionHeader> and 
#            it contains any of <secTags>
#            then its marked as <CvSection>
#    parseLogic
#         -- Function that would be executed for
#            parsing <line list>
#    secTagNameDict
#         -- temp dictionary that stores
#              <SecTag> Vs <SecName>
#---------------------------------------------------

class CvSection:
	def __init__(self, secName, secTags, parseLogic):
		self.secName = secName
		self.secTags = secTags
		self.parseLogic = parseLogic
		self.lineList = []
		self.setSecTagNameDict()

	def setSecTagNameDict(self):
		self.secTagNameDict = {}
		for secTag in self.secTags:
			self.secTagNameDict[secTag] = self.secName

	def getSecName(self):
		return self.secName

	def getSecTagNameDict(self):
		return self.secTagNameDict

	def getLineList(self):
		return self.lineList

	def addLine(self, line):
		self.lineList.append(line)

	def parse(self):
		for line in self.lineList:
			logging.debug('parsing :' + line)

	def __str__(self):
		str1 = '----------------------------------------' + NewLine
		str1 += 'section:' + self.getSecName() + NewLine
		i=0
		for line in self.lineList:
			i += 1
			str1 += '[' + str(i) + '] = ' + line + NewLine

		return str1

#------------------------------------------
# Unit test
#------------------------------------------
class TestCvSection(unittest.TestCase):

	def test_constructor(self):
		# Unique tags
		cvSection = CvSection('sec1', ['tag1', 'tag101'], 'some-func')
		self.assertEqual(2, len(cvSection.getSecTagNameDict()))

		# Non-Unique tags
		cvSection = CvSection('sec2', ['tag22', 'tag22'], 'some-func')
		self.assertEqual(1, len(cvSection.getSecTagNameDict()))

	def test_addLine(self):
		cvSection = CvSection('sec1', ['tag1', 'tag101'], 'some-func')

		line1 = 'this is a test line 1'
		cvSection.addLine(line1)
		self.assertEqual(line1, cvSection.getLineList()[0])
		self.assertEqual(1, len(cvSection.getLineList()))

		line2 = 'this is a test line 2'
		cvSection.addLine(line2)
		self.assertEqual(line2, cvSection.getLineList()[1])

		self.assertEqual(2, len(cvSection.getLineList()))

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSection)
unittest.TextTestRunner(verbosity=2).run(suite)

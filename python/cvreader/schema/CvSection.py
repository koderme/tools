#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from rules.CvSectionParseRules import *



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
#    parseFunc
#         -- Function that would be executed for
#            parsing <line list>
#    parseResult
#         -- dict containing parse results
#    secTagNameDict
#         -- temp dictionary that stores
#              <SecTag> Vs <SecName>
#---------------------------------------------------

class CvSection:
	def __init__(self, secName, secTags, parseFunc=None):
		self.secName = secName
		self.secTags = secTags
		self.parseFunc = parseNoop
		if (parseFunc != None):
			self.parseFunc = parseFunc
		self.setSecTagNameDict()

	def setSecTagNameDict(self):
		self.secTagNameDict = {}
		for secTag in self.secTags:
			self.secTagNameDict[secTag] = self.secName

	def getSecName(self):
		return self.secName

	def getSecTagNameDict(self):
		return self.secTagNameDict

	def getParseFunc(self):
		return self.parseFunc

	def __str__(self):
		return self.secName + ':' + str(self.secTags)+ ':' + str(self.parseFunc)


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


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSection)
unittest.TextTestRunner(verbosity=2).run(suite)

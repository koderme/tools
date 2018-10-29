#!/usr/bin/python3.6

import os
import unittest
import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from rules.CvSectionParseRules import *


logger = logging.getLogger('cvreader')

#---------------------------------------------------
# CvSectionSchema represents 1 section of Cv.
# It stores following metadata
#    secName
#         -- name of the section
#    secTagRe
#         -- Its used to identify start of section.
#         -- if line is identified as <SectionHeader> and 
#            it matches <secTagRe>
#            then its marked as <CvSectionSchema>
#    parseFunc
#         -- Function that would be executed for
#            parsing <line list>
#    parseResult
#         -- dict containing parse results
#---------------------------------------------------

class CvSectionSchema:
	def __init__(self, secName, secTagRe, parseFunc=None):
		self.secName = secName
		self.secTagRe = secTagRe
		self.parseFunc = parseNoop
		if (parseFunc != None):
			self.parseFunc = parseFunc

	def getSecName(self):
		return self.secName

	def getSecTagRe(self):
		return self.secTagRe

	def getParseFunc(self):
		return self.parseFunc

	def __str__(self):
		return self.secName + ':' + str(self.secTagRe)+ ':' + str(self.parseFunc)


#------------------------------------------
# Unit test
#------------------------------------------
class TestCvSectionSchema(unittest.TestCase):

	def test_constructor(self):
		#
		cvSection = CvSectionSchema('sec1', '(tag1|tag2)', 'some-func')
		self.assertEqual('sec1', cvSection.getSecName())
		self.assertEqual('(tag1|tag2)', cvSection.getSecTagRe())
		self.assertEqual('some-func', cvSection.getParseFunc())



# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSectionSchema)
unittest.TextTestRunner(verbosity=2).run(suite)

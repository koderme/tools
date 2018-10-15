#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')

from nltk.tokenize import sent_tokenize, word_tokenize

from common.Utils import *
from Common import *
from CvSection import *
from CvParseRule import *



#-------------------------------------------------------------
# CvParseImpl provides implementation for parsing text CV.
#
#-------------------------------------------------------------
class CvParseImpl:
	schema = CvSchema()

	def __init__(self, inFilepath):

	#--------------------------------------------------------
	# Its parses the specified lines below steps:
	#  1. Builds the CvContent
	#  2. Parses the CvContent
	#--------------------------------------------------------
	def parse(self):
		lineList = Utils.getTextLines(self.inFilepath)

		# Build the content
		content = self.schema.buildContent(lineList)

		# Parse the content
		parseResult = CvParseResult()
		for secName, sentList content.getContentDict().items():
			parseFunc = self.schema.getParseFunc(sectName)	
			attrDict = parseResult.getSectionDict(sectName)
			parseFunc(sentList, attrDict)

		return parseResult

#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestCvParseImpl(unittest.TestCase):

	def test_default_dict_size(self):

		cvSecs = CvParseImpl()

		# verify dict size
		self.assertNotEqual(0, len(cvSecs.get_secTag_secName_dict()))
		self.assertEqual(11, len(cvSecs.get_secName_cvSection_dict()))

	def test_findCvSection(self):

		cvSecs = CvParseImpl()

		cvSec = cvSecs.findCvSection('personal')
		self.assertEqual(Ref.Section.personal.name, cvSec.getSecName())
		cvSec = cvSecs.findCvSection('aboutme')
		self.assertEqual(Ref.Section.personal.name, cvSec.getSecName())

		cvSec = cvSecs.findCvSection('professional summary')
		self.assertEqual(Ref.Section.summary.name, cvSec.getSecName())

		cvSec = cvSecs.findCvSection('career history')
		self.assertEqual(Ref.Section.workhistory.name, cvSec.getSecName())
		cvSec = cvSecs.findCvSection('work history')
		self.assertEqual(Ref.Section.workhistory.name, cvSec.getSecName())
		cvSec = cvSecs.findCvSection('experience')
		self.assertEqual(Ref.Section.workhistory.name, cvSec.getSecName())

		cvSec = cvSecs.findCvSection('project summary')
		self.assertEqual(Ref.Section.project.name, cvSec.getSecName())

		cvSec = cvSecs.findCvSection('address')
		self.assertEqual(Ref.Section.address.name, cvSec.getSecName())
		cvSec = cvSecs.findCvSection('residence')
		self.assertEqual(Ref.Section.address.name, cvSec.getSecName())

	def test_findCvSection_default(self):

		cvSecs = CvParseImpl()

		cvSec = cvSecs.findCvSection('XyZ Abc ')
		self.assertEqual(None, cvSec)

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
logging.basicConfig(level=logging.INFO)
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvParseImpl)
unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')

from nltk.tokenize import sent_tokenize, word_tokenize

from common.Utils import *
from Common import *
from schema.CvSchema import *
from model.CvParseResult import *
from rules.CvParseRules import *

from CvParse import *


#-------------------------------------------------------------
# CvParseImpl provides implementation for parsing text CV.
#
#-------------------------------------------------------------
class CvParseImpl(CvParse):
	schema = CvSchema()

	def __init__(self, inFilepath):
		self.inFilepath = inFilepath
		logging.debug('schema:' + str(CvParseImpl.schema))

	#--------------------------------------------------------
	# Its parses the specified lines below steps:
	#  1. Builds the CvContent
	#  2. Parses the CvContent
	#--------------------------------------------------------
	def parse(self):
		lineList = Utils.getTextLines(self.inFilepath)

		# Build the content
		content = CvParseImpl.schema.buildContent(lineList)

		logging.info('--------content------------')
		logging.info(str(content))

		# Parse the content
		parseResult = CvParseResult()
		for secName, sentList in content.getContentDict().items():
			parseFunc = CvParseImpl.schema.getParseFunc(secName)	
			attrDict = parseResult.getSectionDict(secName)

			if (parseFunc == None):
				logging.error('No parse function defined for section:' + secName)
				continue

			parseFunc(sentList, attrDict)

		return parseResult

#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestCvParseImpl(unittest.TestCase):

	def test_default_dict_size(self):
		pass


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
logging.basicConfig(level=logging.INFO)
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvParseImpl)
unittest.TextTestRunner(verbosity=2).run(suite)

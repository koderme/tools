#!/usr/bin/python3.6

import os
import unittest
import sys
sys.path.append('..')

from nltk.tokenize import sent_tokenize, word_tokenize

from common.Utils import *
from schema.CvSchema import *
from model.CvParseResult import *
from rules.CvParseRules import *

from CvParse import *

logger = logging.getLogger('cvreader')

#-------------------------------------------------------------
# CvParseImpl provides implementation for parsing text CV.
#
#-------------------------------------------------------------
class CvParseImpl(CvParse):
	schema = CvSchema()

	def __init__(self, inFilepath):
		self.inFilepath = inFilepath
		logger.debug('schema:' + str(CvParseImpl.schema))

	#--------------------------------------------------------
	# Its parses the specified lines below steps:
	#  1. Builds the CvContent
	#  2. Parses the CvContent
	#--------------------------------------------------------
	def parse(self):
		lineList = Utils.getTextLines(self.inFilepath)

		# Build the content
		content = CvParseImpl.schema.buildContent(lineList)

		logger.info('--------content------------')
		logger.info('file:'  + self.inFilepath)
		logger.info(str(content))

		# Parse the content
		parseResult = CvParseResult()
		logger.info('number of sections in content :' + str(len(content.getSecContentList())))
		for secContent in content.getSecContentList():
			parseFunc = CvParseImpl.schema.getParseFunc(secContent.getSecName())
			attrDict = parseResult.getSectionDict(secContent.getSecName())

			if (parseFunc == None):
				logger.error('No parse function defined for section:' + secName)
				continue

			parseFunc(secContent.getLineList(), attrDict)

		return parseResult

#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestCvParseImpl(unittest.TestCase):

	def test_constr(self):
		pass


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvParseImpl)
unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/python3.6

import os
import unittest
import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from rules.CvParseRules import *
from model.ReferenceData import *
from model.CvContent import *
from schema.CvSectionSchema import *
from schema.CvSchemaBuilder import *

logger = logging.getLogger('cvreader')

#-------------------------------------------------------------
# CvSchema holds the structure/metadata parsing content.
# For parsing CV, one must first build content.
# Once content is build, call parse() to get CvParseResult
#
# Composition of CvSchema:
#    1. CvSchema = CvSectionSchema + CvSectionSchema + ...
#    2.  
#        * CvSectionSchema starts when any of <SecTag> defined in CvSectionSchema is found.
#        * CvSectionSchema ends another Section starts.
#
# Metadata from CvSectionSchema is used to form below dictionaries:
#
# secList 
#    List of section in the order of creation
#
# secDict
#    This dictionary stores <SecName> vs <CvSectionSchema> 
#    for all the CvSectionSchema.
#-------------------------------------------------------------
class CvSchema:
	def __init__(self):
		self.secList = []
		self.secDict = {}
		self.buildSchema()

	#--------------------------------------------------------
	# This is internal method
	# It builds the schema
	#--------------------------------------------------------
	def buildSchema(self):
		for section in CvSchemaBuilder.buildSectionsForSchema():
			self.updateSchema(section)

	#--------------------------------------------------------
	# This is internal method
	# It updates the dictionaries. 
	# @param section CvSectionSchema that hold metadata.
	#--------------------------------------------------------
	def updateSchema(self, section):
		self.secList.append(section)
		self.secDict[section.getSecName()] = section
		

	#--------------------------------------------------------
	# Below is the logic used:	
	# 1. Search the <SecTag> in the <line>.
	#      If match is found, corr's <CvSectionSchema> becomes current.
	#      else it continues to use prev <CvSectionSchema>
	# 2. Add [line] to identfied CvSchema
	#
	# @param listList List of lines to be parsed
	# @return CvContent Dictionary of <sectionName, sentence[]>
	#--------------------------------------------------------
	def buildContent(self, lineList):
		content = CvContent()

		currCvSec = self.getDetaultCvSectionSchema()
		newSectionFound = False
		for line in lineList:

			line = line.strip()
			if (len(line) <= 1):
				continue
			
			# Find matching CvSectionSchema	
			foundCvSec = self.findCvSectionSchema(line)

			if (foundCvSec == None):
				content.addLine(currCvSec.getSecName(), line, newSectionFound)
				newSectionFound = False
			# Found default
			elif ( foundCvSec.getSecName() == Ref.Section.default.name ):
				# Ignore intermediate default section
				if (currCvSec.getSecName() == Ref.Section.default.name):
					currCvSec = foundCvSec
					newSectionFound = True
				
			else:
				logger.debug('changing section to [' + foundCvSec.getSecName() + '] because of line :' + line)
				currCvSec = foundCvSec
				newSectionFound = True

			logger.debug("section [" + currCvSec.getSecName() + "] ====> [" + line + "]")
		return content

	#--------------------------------------------------------
	# Find matching section.
	# Logic:
	#    1. Is <line> a SectionHeader
	#    2. Does <line> contains [SecTag]
	# If [1] and [2] are true, corr's CvSectionSchema
	# is returned, else None.
	#
	#--------------------------------------------------------
	def findCvSectionSchema(self, line):
		lineType = CvParseRules.getLineType(line)
		logger.debug("line [" + line + "] is a " + lineType)
		if (lineType != Ref.LineType.SectionHeader.name):
			return None

		# Line is SectionHeader

		# Proceed with secTag match
		for sec in self.secList:
			if (Utils.search(sec.getSecTagRe(), line)):
				logger.debug('matching section found:' + sec.getSecName())
				return sec

		logger.debug("line [" + line + "] doesn't map to any Section")
		return None

	# Helper methods
	def getDetaultCvSectionSchema(self):
		return self.secDict[Ref.Section.default.name]

	def getSecDict(self):
		return self.secDict

	def getParseFunc(self, secName):
		section = self.secDict.get(secName, None)
		if (section == None):
			logger.warn('section[' + secName + '] not found')
			return None

		return section.getParseFunc()

	def __str__(self):
		retStr = ''
		for secName, cvSec in self.secDict.items():
			retStr += str(cvSec) + '\n'

		return retStr
		

#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestCvSchema(unittest.TestCase):

	def test_default_dict_size(self):

		schema = CvSchema()

		# verify dict size
		self.assertNotEqual(0, len(schema.getSecDict()))
		self.assertEqual(10, len(schema.getSecDict()))

	def test_findCvSectionSchema(self):

		schema = CvSchema()

		cvSec = schema.findCvSectionSchema('personal')
		self.assertEqual(Ref.Section.personal.name, cvSec.getSecName())
		cvSec = schema.findCvSectionSchema('aboutme')
		self.assertEqual(Ref.Section.personal.name, cvSec.getSecName())

		cvSec = schema.findCvSectionSchema('professional summary')
		self.assertEqual(Ref.Section.summary.name, cvSec.getSecName())

		cvSec = schema.findCvSectionSchema('career history')
		self.assertEqual(Ref.Section.workhistory.name, cvSec.getSecName())
		cvSec = schema.findCvSectionSchema('work history')
		self.assertEqual(Ref.Section.workhistory.name, cvSec.getSecName())
		cvSec = schema.findCvSectionSchema('experience')
		self.assertEqual(Ref.Section.workhistory.name, cvSec.getSecName())

		cvSec = schema.findCvSectionSchema('project summary')
		self.assertEqual(Ref.Section.project.name, cvSec.getSecName())

		cvSec = schema.findCvSectionSchema('address')
		self.assertEqual(Ref.Section.address.name, cvSec.getSecName())
		cvSec = schema.findCvSectionSchema('residence')
		self.assertEqual(Ref.Section.address.name, cvSec.getSecName())

	def test_findCvSectionSchema_default(self):

		schema = CvSchema()

		cvSec = schema.findCvSectionSchema('XyZ Abc ')
		defaultSec = CvSchemaBuilder.getDefaultSection()
		self.assertEqual(None, cvSec)

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSchema)
unittest.TextTestRunner(verbosity=2).run(suite)

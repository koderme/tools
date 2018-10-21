#!/usr/bin/python3.5

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
from schema.CvSection import *
from schema.CvSchemaBuilder import *

logger = logging.getLogger('cvreader')

#-------------------------------------------------------------
# CvSchema holds the structure/metadata parsing content.
# For parsing CV, one must first build content.
# Once content is build, call parse() to get CvParseResult
#
# Composition of CvSchema:
#    1. CvSchema = CvSection + CvSection + ...
#    2.  
#        * CvSection starts when any of <SecTag> defined in CvSection is found.
#        * CvSection ends another Section starts.
#
# Metadata from CvSection is used to form below dictionaries:
#
# secList 
#    List of section in the order of creation
#
# secDict
#    This dictionary stores <SecName> vs <CvSection> 
#    for all the CvSection.
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
	# @param section CvSection that hold metadata.
	#--------------------------------------------------------
	def updateSchema(self, section):
		self.secList.append(section)
		self.secDict[section.getSecName()] = section
		

	#--------------------------------------------------------
	# Below is the logic used:	
	# 1. Search the <SecTag> in the <line>.
	#      If match is found, corr's <CvSection> becomes current.
	#      else it continues to use prev <CvSection>
	# 2. Add [line] to identfied CvSchema
	#
	# @param listList List of lines to be parsed
	# @return CvContent Dictionary of <sectionName, sentence[]>
	#--------------------------------------------------------
	def buildContent(self, lineList):
		content = CvContent()

		currCvSec = self.getDetaultCvSection()
		for line in lineList:


			line = line.strip()
			if (len(line) <= 1):
				continue
			
			# Find matching CvSection	
			foundCvSec = self.findCvSection(line)

			if (foundCvSec == None):
				content.addLine(currCvSec.getSecName(), line)
			# Found default
			elif ( foundCvSec.getSecName() == Ref.Section.default.name ):
				# Ignore intermediate default section
				if (currCvSec.getSecName() == Ref.Section.default.name):
					currCvSec = foundCvSec
			else:
				logger.debug('changing section to [' + foundCvSec.getSecName() + '] because of line :' + line)
				currCvSec = foundCvSec

			logger.debug("section [" + currCvSec.getSecName() + "] ====> [" + line + "]")
		return content

	#--------------------------------------------------------
	# Find matching section.
	# Logic:
	#    1. Is <line> a SectionHeader
	#    2. Does <line> contains [SecTag]
	# If [1] and [2] are true, corr's CvSection
	# is returned, else None.
	#
	#--------------------------------------------------------
	def findCvSection(self, line):
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
	def getDetaultCvSection(self):
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

	def test_findCvSection(self):

		schema = CvSchema()

		cvSec = schema.findCvSection('personal')
		self.assertEqual(Ref.Section.personal.name, cvSec.getSecName())
		cvSec = schema.findCvSection('aboutme')
		self.assertEqual(Ref.Section.personal.name, cvSec.getSecName())

		cvSec = schema.findCvSection('professional summary')
		self.assertEqual(Ref.Section.summary.name, cvSec.getSecName())

		cvSec = schema.findCvSection('career history')
		self.assertEqual(Ref.Section.workhistory.name, cvSec.getSecName())
		cvSec = schema.findCvSection('work history')
		self.assertEqual(Ref.Section.workhistory.name, cvSec.getSecName())
		cvSec = schema.findCvSection('experience')
		self.assertEqual(Ref.Section.workhistory.name, cvSec.getSecName())

		cvSec = schema.findCvSection('project summary')
		self.assertEqual(Ref.Section.project.name, cvSec.getSecName())

		cvSec = schema.findCvSection('address')
		self.assertEqual(Ref.Section.address.name, cvSec.getSecName())
		cvSec = schema.findCvSection('residence')
		self.assertEqual(Ref.Section.address.name, cvSec.getSecName())

	def test_findCvSection_default(self):

		schema = CvSchema()

		cvSec = schema.findCvSection('XyZ Abc ')
		defaultSec = CvSchemaBuilder.getDefaultSection()
		self.assertNotEqual(None, cvSec)
		self.assertEqual(defaultSec.getSecName(), cvSec.getSecName())

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSchema)
unittest.TextTestRunner(verbosity=2).run(suite)

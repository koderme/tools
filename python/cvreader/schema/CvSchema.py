#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from Common import *
from rules.CvParseRules import *
from model.ReferenceData import *

from CvSection import *
from CvSchemaBuilder import *

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
# secTag_secName_dict 
#    This dictionary stores <SecTag> Vs <SecName> for
#    all the CvSection.
#
# secName_cvSection_dict
#    This dictionary stores <SecName> vs <CvSection> 
#    for all the CvSection.
#-------------------------------------------------------------
class CvSchema:
	def __init__(self):
		self.secTag_secName_dict = {}
		self.secName_cvSection_dict = {}
		self.buildSchema()

	#--------------------------------------------------------
	# This is internal method
	# It builds the schema
	#--------------------------------------------------------
	def buildSchema(self):
		for section in CvSchemaBuilder.buildSectionsForSchema():
			self.updateDicts(section)

	#--------------------------------------------------------
	# This is internal method
	# It updates the dictionaries. 
	# @param section CvSection that hold metadata.
	#--------------------------------------------------------
	def updateDicts(self, section):
		self.secTag_secName_dict.update(section.getSecTagNameDict())
		self.secName_cvSection_dict[section.getSecName()] = section
		

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

			newSectionFound = False

			line = line.strip()
			if (len(line) <= 1):
				continue
			
			# Find matching CvSection	
			foundCvSec = self.findCvSection(line)

			if (foundCvSec != None):
				newSectionFound = True
				currCvSec = foundCvSec

			logging.debug("section [" + currCvSec.getSecName() + "] ====> [" + line + "]")
			if (not newSectionFound):
				currCvSec.addLine(line)
				content.addSentence(currCvSec.getSecName(), line)

		return content

	#--------------------------------------------------------
	#
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
		logging.debug("line [" + line + "] has line type" + lineType)
		if (lineType != Ref.LineType.SectionHeader.name):
			logging.debug("line [" + line + "] is not SectionHeader")
			return None

		# Line is SectionHeader

		# Proceed with secTag match
		for secTag,secName in self.secTag_secName_dict.items():
			if (line.find(secTag) != -1):
				logging.debug('matching section found:' + secName)
				return self.secName_cvSection_dict[secName]

		logging.debug("line [" + line + "] doesn't map to any Section")
		return None

	# Helper methods
	def getDetaultCvSection(self):
		return self.secName_cvSection_dict[Ref.Section.default.name]

	def get_secTag_secName_dict(self):
		return self.secTag_secName_dict

	def get_secName_cvSection_dict(self):
		return self.secName_cvSection_dict

	def getParseFunc(self, secName):
		section = self.secName_cvSection_dict.get(secName, None)
		if (section == None):
			logging.warn('section[' + secName + '] not found')
			return None
		else
			section.getParseFunc()
#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestCvSchema(unittest.TestCase):

	def test_default_dict_size(self):

		schema = CvSchema()

		# verify dict size
		self.assertNotEqual(0, len(schema.get_secTag_secName_dict()))
		self.assertEqual(11, len(schema.get_secName_cvSection_dict()))

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
		self.assertEqual(None, cvSec)

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
logging.basicConfig(level=logging.INFO)
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSchema)
unittest.TextTestRunner(verbosity=2).run(suite)

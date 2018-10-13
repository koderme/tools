#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')

from nltk.tokenize import sent_tokenize, word_tokenize

from common.Utils import *
from Common import *
from ReferenceData import *
from CvSection import *
from CvParseRule import *


Section =  Enum('', 'unknown default personal summary skill workhistory project education certification address objective')

#---------------------------------------------------
# CvSections represent collection of CvSection
# NOTE:
# * CvSection starts when <SecTag> defined in CvSection are found.
# * CvSection ends another Section starts.
#
# It use metadata from CvSection to form 2 dictionaries.
#
# secTag_secName_dict 
#    This dictionary stores <SecTag> Vs <SecName> for
#    all the CvSection.
#
# secName_cvSection_dict
#    This dictionary stores <SecName> vs <CvSection> 
#    for all the CvSection.
#---------------------------------------------------
class CvSections:
	def __init__(self):
		self.secTag_secName_dict = {}
		self.secName_cvSection_dict = {}
		self.buildCvSchema()

	def updateDicts(self, cvs):
		self.secTag_secName_dict.update(cvs.getSecTagNameDict())
		self.secName_cvSection_dict[cvs.getSecName()] = cvs
		

	# It builds the schema for CV.
	def buildCvSchema(self):
		cvs = CvSection(Section.unknown.name, [])
		self.updateDicts(cvs)

		cvs = CvSection(Section.default.name, [])
		self.updateDicts(cvs)

		cvs = CvSection(Section.personal.name, ['personal', 'aboutme'])
		self.updateDicts(cvs)

		cvs = CvSection(Section.summary.name, ['professional summary', 'profile summary'])
		self.updateDicts(cvs)

		cvs = CvSection(Section.skill.name, ['skill'])
		self.updateDicts(cvs)

		cvs = CvSection(Section.workhistory.name, ['work history', 'career history', 'experience'])
		self.updateDicts(cvs)

		cvs = CvSection(Section.project.name, ['project summary', 'assignment history'])
		self.updateDicts(cvs)

		cvs = CvSection(Section.education.name, ['qualification', 'education', 'scholastic'])
		self.updateDicts(cvs)

		cvs = CvSection(Section.certification.name, ['certification'])
		self.updateDicts(cvs)

		cvs = CvSection(Section.address.name, ['address', 'residence'])
		self.updateDicts(cvs)

		cvs = CvSection(Section.objective.name, ['objective'])
		self.updateDicts(cvs)

		
	# Below is the logic used:	
	# 1. Search the <SecTag> in the <line>.
	#      If match is found, corr's <CvSection> becomes current.
	#      else it continues to use prev <CvSection>
	# 2. Add [line] to identfied CvSections
	def parse(self, lineList):
		currCvSec = self.getDetaultCvSection()
		for line in lineList:

			line = line.strip()
			if (len(line) <= 1):
				continue
			
			# Find matching CvSection	
			foundCvSec = self.findCvSection(line)

			if (foundCvSec != None):
				currCvSec = foundCvSec

			logging.debug("section [" + currCvSec.getSecName() + "] ====> [" + line + "]")
			currCvSec.addLine(line)

		for k,v in self.secName_cvSection_dict.items():
			v.parse()

	#
	# Find matching section.
	# Logic:
	#    1. Is <line> a SectionHeader
	#    2. Does <line> contains [SecTag]
	# If [1] and [2] are true, corr's CvSection
	# is returned, else None.
	#
	def findCvSection(self, line):
		lineType = CvParseRule.getLineType(line)
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
		return self.secName_cvSection_dict[Section.default.name]

	def get_secTag_secName_dict(self):
		return self.secTag_secName_dict

	def get_secName_cvSection_dict(self):
		return self.secName_cvSection_dict

	def show(self):
		logging.info('-------------parsed cv content----------------')
		for k,v in self.secName_cvSection_dict.items():
			logging.info(str(v))

# Do the unit tests
class TestCvSections(unittest.TestCase):

	def test_default_dict_size(self):

		cvSecs = CvSections()

		# verify dict size
		self.assertNotEqual(0, len(cvSecs.get_secTag_secName_dict()))
		self.assertEqual(11, len(cvSecs.get_secName_cvSection_dict()))

	def test_findCvSection(self):

		cvSecs = CvSections()

		cvSec = cvSecs.findCvSection('personal')
		self.assertEqual(Section.personal.name, cvSec.getSecName())
		cvSec = cvSecs.findCvSection('aboutme')
		self.assertEqual(Section.personal.name, cvSec.getSecName())

		cvSec = cvSecs.findCvSection('professional summary')
		self.assertEqual(Section.summary.name, cvSec.getSecName())

		cvSec = cvSecs.findCvSection('career history')
		self.assertEqual(Section.workhistory.name, cvSec.getSecName())
		cvSec = cvSecs.findCvSection('work history')
		self.assertEqual(Section.workhistory.name, cvSec.getSecName())
		cvSec = cvSecs.findCvSection('experience')
		self.assertEqual(Section.workhistory.name, cvSec.getSecName())

		cvSec = cvSecs.findCvSection('project summary')
		self.assertEqual(Section.project.name, cvSec.getSecName())

		cvSec = cvSecs.findCvSection('address')
		self.assertEqual(Section.address.name, cvSec.getSecName())
		cvSec = cvSecs.findCvSection('residence')
		self.assertEqual(Section.address.name, cvSec.getSecName())

	def test_findCvSection_default(self):

		cvSecs = CvSections()

		cvSec = cvSecs.findCvSection('XyZ Abc ')
		self.assertEqual(None, cvSec)

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
logging.basicConfig(level=logging.INFO)
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSections)
unittest.TextTestRunner(verbosity=2).run(suite)

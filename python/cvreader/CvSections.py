#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')

from nltk.tokenize import sent_tokenize, word_tokenize

from common.Utils import *
from CvSection import *


Section =  Enum('', 'unknown default personal summary skill workhistory project education certification address objective')

#---------------------------------------------------
# CvSections represent collection of CvSection
# NOTE:
# * CvSection starts when tags defined in CvSection are found.
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
		cvs = CvSection(Section.unknown.name, [], 'func1')
		self.updateDicts(cvs)

		cvs = CvSection(Section.default.name, [], 'func1')
		self.updateDicts(cvs)

		cvs = CvSection(Section.personal.name, ['personal', 'aboutme'], 'func1')
		self.updateDicts(cvs)

		cvs = CvSection(Section.summary.name, ['professional summary', 'profile summary'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection(Section.skill.name, ['skill'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection(Section.workhistory.name, ['work history', 'career history', 'experience'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection(Section.project.name, ['project summary'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection(Section.education.name, ['qualification', 'education', 'scholastic'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection(Section.certification.name, ['certification'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection(Section.address.name, ['address', 'residence'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection(Section.objective.name, ['objective'], 'func2')
		self.updateDicts(cvs)


	# Find matching section
	# Here, the sentence is tokenized, and each word is
	# matched with tags (defined for CvSection).
	# When match occurs, corr's CvSection is returned.
	# For no match, None is returned
	def findCvSectionByWords(self, sentence):
		wordList = word_tokenize(sentence)
		for word in wordList:
			matchingSecName = self.secTag_secName_dict.get(word, Section.unknown.name)
			if (matchingSecName != Section.unknown.name):
				logging.debug('matching section found:' + str(matchingSecName))
				return self.secName_cvSection_dict[matchingSecName]

		return None

	# Find matching section.
	# The collection of tags are matched with sentence.
	# If matching tag is found, corr's CvSection is
	# returned.
	def findCvSection(self, sentence):
		for secTag,secName in self.secTag_secName_dict.items():
			if (sentence.find(secTag) != -1):
				logging.debug('matching section found:' + secName)
				return self.secName_cvSection_dict[secName]

		return None
			
	# 1. Identify sections
	# 2. Add sentences to identfied CvSections
	def parse(self, sentenceList):
		cvSec = self.getDetaultCvSection()
		for sentence in sentenceList:
			# Find matching CvSection	
			foundCvSec = self.findCvSection(sentence)

			if (foundCvSec != None):
				cvSec = foundCvSec

			logging.info("section [" + cvSec.getSecName() + "] ====> [" + sentence + "]")
			cvSec.addSentence(sentence)

	# Helper methods
	def getDetaultCvSection(self):
		return self.secName_cvSection_dict[Section.default.name]

	def get_secTag_secName_dict(self):
		return self.secTag_secName_dict

	def get_secName_cvSection_dict(self):
		return self.secName_cvSection_dict

	def show(self):
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

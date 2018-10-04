#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')

from nltk.tokenize import sent_tokenize, word_tokenize

from common.Utils import *
from CvSection import *


Section =  Enum('', 'unknown personal summary skill work-history project certification default')

#---------------------------------------------------
# CvSections represent collection of CvSection
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
		cvs = CvSection('personal', ['personal', 'aboutme'], 'func1')
		self.updateDicts(cvs)

		cvs = CvSection('summary', ['summary', 'professional'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection('skill', ['skill'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection('work-history', ['work', 'experience'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection('project', ['project'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection('certification', ['certification'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection('address', ['address', 'residence'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection('qualification', ['qualification', 'education', 'scholastic'], 'func2')
		self.updateDicts(cvs)

		cvs = CvSection('objective', ['objective'], 'func2')
		self.updateDicts(cvs)


	# Find matching section
	# A CvSection is said to be found if any words
	# in sentence match the identifying tags defined for that CvSection.
	# For no match, None is returned
	def findCvSection(self, sentence):
		wordList = word_tokenize(sentence)
		for word in wordList:
			matchingSecName = self.secTag_secName_dict.get(word, Section.unknown.name)
			if (matchingSecName != Section.unknown.name):
				logging.debug('matching section found:' + str(matchingSecName))
				return self.secName_cvSection_dict[matchingSecName]

		return None
			
	# 1. Identify sections
	# 2. Add sentences to identfied CvSections
	def parseOne(self, sentenceList):
		cvSec = self.getDetaultCvSection()
		for sentence in sentenceList:
			# Find matching CvSection	
			foundCvSec = self.find(sentence)

			if (cvSec != None):
				cvSec = foundCvSec

			cvSec.addSentence(sentence)

	# Returns the default CvSection
	def getDetaultCvSection(self):
		return self.secName_cvSection_dict[Section.default.name]

	def get_secTag_secName_dict(self):
		return self.secTag_secName_dict

	def get_secName_cvSection_dict(self):
		return self.secName_cvSection_dict

# Do the unit tests
class TestCvSections(unittest.TestCase):

	def test_default_dict_size(self):

		cvSecs = CvSections()

		# verify dict size
		self.assertNotEqual(0, len(cvSecs.get_secTag_secName_dict()))
		self.assertEqual(9, len(cvSecs.get_secName_cvSection_dict()))

	def test_findCvSection(self):

		cvSecs = CvSections()

		cvSec = cvSecs.findCvSection('personal')
		self.assertEqual(Section.personal.name, cvSec.getSecName())
		cvSec = cvSecs.findCvSection('aboutme')
		self.assertEqual(Section.personal.name, cvSec.getSecName())

		cvSec = cvSecs.findCvSection('summary')
		self.assertEqual(Section.summary.name, cvSec.getSecName())
		cvSec = cvSecs.findCvSection('professional')
		self.assertEqual(Section.summary.name, cvSec.getSecName())

		cvSec = cvSecs.findCvSection('experience summary ')
		self.assertEqual('work-history', cvSec.getSecName())

		cvSec = cvSecs.findCvSection('work')
		self.assertEqual('work-history', cvSec.getSecName())
		cvSec = cvSecs.findCvSection('experience')
		self.assertEqual('work-history', cvSec.getSecName())

		cvSec = cvSecs.findCvSection('address')
		self.assertEqual('address', cvSec.getSecName())
		cvSec = cvSecs.findCvSection('residence')
		self.assertEqual('address', cvSec.getSecName())

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

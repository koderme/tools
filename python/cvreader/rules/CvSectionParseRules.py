#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')
sys.path.append('../..')

from model.ReferenceData import *
from rules.CvParseRules import *
from common.Utils import *

#-----------------------------------------------------
# Helper functions
#-----------------------------------------------------
def split_1_then_2(line, splitChar1, splitChar2):
	firstSplitToks = line.split(splitChar1)

	# Doesnt have splitChar1
	if (len(firstSplitToks) == 1):
		return firstSplitToks[0].split(splitChar2)

	# Has splitChar1
	return firstSplitToks[1].split(splitChar2)
	
#-----------------------------------------------------
# Nothing to be done
#-----------------------------------------------------
def parseNoop(sentenceList, prDict):
	pass

#-----------------------------------------------------
# It parses the lines in specified CvSection
# The lines being parsed are expected in below format:
# e.g.: operating systems     :    windows  and unix
# e.g.: core  java, servlets, jsp, jdbc
#
# @param sentenceList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parseSkill(sentenceList, prDict):
	skillList = []
	for line in sentenceList:
		skillList.extend(split_1_then_2(line, ':', ','))

	prDict[Ref.Section.skill.name] = skillList

#-----------------------------------------------------
# It parses the lines in specified CvSection
# Logic:
#   1. It extracts email
#   2. It extracts phone
#   3. If above extraction has no results
#      it assumes this line to be name.
#
# @param sentenceList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parseDefault(sentenceList, prDict):
	emailIdList = []
	phoneList = []
	name = ''
	for line in sentenceList:

		# Extract email
		if (len(emailIdList) == 0):
			emailIdList = CvParseRules.getEmail(line)

		if (len(phoneList) == 0):
			phoneList = CvParseRules.getPhone(line)

		
		if ((len(emailIdList) == 0) and (len(phoneList) == 0)):
			name = line

	# Remove tags from name
	name = split_1_then_2(name, ':', '__anything__')[0].strip()

	prDict['emailid'] = emailIdList
	prDict['phone'] = phoneList
	prDict['name'] = name

#-----------------------------------------------------
# It parses the lines in specified CvSection
# Logic:
#   1. It extracts location
#   2. It extracts DOB
#
# @param sentenceList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parsePersonal(sentenceList, prDict):

	location = Ref.DefaultLocation

	for line in sentenceList:
		# Fetch location
		if (location != Ref.DefaultLocation):
			break

		location = Ref.getLocation(line)
	
	prDict['location'] = location

#------------------------------------------
# Unit test
#------------------------------------------
class TestThisClass(unittest.TestCase):

	# ----------- parseSkill ----------
	def test_parseSkill_with_colon(self):

		lines = []
		lines.append('operating systems     :    windows  and unix')
		lines.append('j2ee  technologies    :    core  java, servlets, jsp, jdbc')
		lines.append('frameworks   /methodologies   :    spring,   hibernate')

		prDict = {}
		parseSkill(lines, prDict)

		self.assertEqual(1, len(prDict))
		self.assertEqual(7, len(prDict[Ref.Section.skill.name]))

	# ----------- parseSkill ----------
	def test_parseSkill_nocolon(self):

		lines = []
		lines.append('windows  and unix')
		lines.append('core  java, servlets, jsp, jdbc')
		lines.append('spring,   hibernate')

		prDict = {}
		parseSkill(lines, prDict)

		self.assertEqual(1, len(prDict))
		self.assertEqual(7, len(prDict[Ref.Section.skill.name]))

	# ----------- parseDefault ----------
	def test_parseDefault(self):

		lines = []
		lines.append('name : First Last')
		lines.append('email : first.last@gmail.com')
		lines.append('mobile : +91 1112223344, 2223334455')

		prDict = {}
		parseDefault(lines, prDict)
		self.assertEqual(3, len(prDict))
		self.assertEqual('first.last@gmail.com', prDict['emailid'][0])
		#self.assertEqual('+91 1112223344', cvSec.getParseResult()['phone'][0])
		self.assertEqual('First Last', prDict['name'])

	# ----------- parseDefault ----------
	def test_parseDefault_wo_token(self):

		lines = []
		lines.append('First Last')
		lines.append('first.last@gmail.com')
		lines.append('+91 1112223344, 2223334455')

		prDict = {}
		parseDefault(lines, prDict)
		self.assertEqual(3, len(prDict))
		self.assertEqual('first.last@gmail.com', prDict['emailid'][0])
		#self.assertEqual('+91 1112223344', cvSec.getParseResult()['phone'][0])
		self.assertEqual('First Last', prDict['name'])

	# ----------- parsePersonal ----------
	def test_parsePersonal(self):

		lines = []
		lines.append('languages known     :   english, hindi,kannada')
		lines.append('permanent address  :   #14,3rd floor, 4th cross, rahamath nagar, rt nagar, bangalore-32 ')
		lines.append('place:            			signature')
		lines.append('bangalore (karnataka)     syed younus')

		prDict = {}
		parsePersonal(lines, prDict)
		self.assertEqual(1, len(prDict))
		self.assertEqual('bangalore', prDict['location'])


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestThisClass)
unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from model.ReferenceData import *
from rules.CvParseRules import *

logger = logging.getLogger('cvreader')

Attr =  Enum('', 'value emailid name phone')

#-----------------------------------------------------
# Split by splitChar1.
# If first split results in 1 token,
#    nextSplitTok = first token is used.
#  else
#    nextSplitTok = second token is used.
# nextSplitTok is then splitted by splitChar2
#-----------------------------------------------------
def split_1_then_2(line, splitChar1, splitChar2):
	firstSplitToks = line.split(splitChar1)

	# Doesnt have splitChar1
	if (len(firstSplitToks) == 1):
		return Utils.stripWordsInList(firstSplitToks[0].split(splitChar2))

	# Has splitChar1
	return Utils.stripWordsInList(firstSplitToks[1].split(splitChar2))
	
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

	prDict[Attr.value.name] = Utils.removeDups(skillList)

#-----------------------------------------------------
# It parses the lines in specified CvSection
# The lines being parsed are expected in below format:
# e.g.: operating systems     :    windows  and unix
# e.g.: core  java, servlets, jsp, jdbc
#
# @param sentenceList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parseEducation(sentenceList, prDict):
	eduList = []
	for line in sentenceList:
		temp1 = re.sub('b\.\s*e\.*\s+', 'be ', line.lower())
		temp2 = re.sub('b\.\s*tech\.*\s+', 'btech ', temp1)

		logger.debug('massaged-line:' +temp2)
		eduList.extend(Ref.findEducation(temp2))

	prDict[Attr.value.name] = Utils.removeDups(eduList)

	logger.debug('prdict:' + str(prDict))

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

	prDict[Attr.emailid.name] = emailIdList
	prDict[Attr.phone.name] = phoneList
	prDict[Attr.name.name] = name

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

	locationList = []

	for line in sentenceList:

		currLocList = Ref.findLocation(line)
		logger.debug('location:' + str(currLocList))
	
		locationList.extend(currLocList)
	
	prDict[Attr.value.name] = Utils.removeDups(locationList)

#------------------------------------------
# Unit test
#------------------------------------------
class TestCvSectionParseRules(unittest.TestCase):

	# ----------- parseSkill ----------
	def test_parseSkill_with_colon(self):

		lines = []
		lines.append('operating systems     :    windows  and unix')
		lines.append('j2ee  technologies    :    core  java, servlets, jsp, jdbc')
		lines.append('frameworks   /methodologies   :    spring,   hibernate')

		prDict = {}
		parseSkill(lines, prDict)

		self.assertEqual(1, len(prDict))
		self.assertEqual(7, len(prDict[Attr.value.name]))

	# ----------- parseSkill ----------
	def test_parseSkill_nocolon(self):

		lines = []
		lines.append('windows  and unix')
		lines.append('core  java, servlets, jsp, jdbc')
		lines.append('spring,   hibernate')

		prDict = {}
		parseSkill(lines, prDict)

		self.assertEqual(1, len(prDict))
		self.assertEqual(7, len(prDict[Attr.value.name]))

	# ----------- parseDefault ----------
	def test_parseDefault(self):

		lines = []
		lines.append('name : First Last')
		lines.append('email : first.last@gmail.com')
		lines.append('mobile : +91 1112223344, 2223334455')

		prDict = {}
		parseDefault(lines, prDict)
		self.assertEqual(3, len(prDict))
		self.assertEqual('first.last@gmail.com', prDict[Attr.emailid.name][0])
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
		self.assertEqual('first.last@gmail.com', prDict[Attr.emailid.name][0])
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
		self.assertEqual(2, len(prDict[Attr.value.name]))
		self.assertEqual(True , 'bangalore' in prDict[Attr.value.name])

	# ----------- parseEducation ----------
	def test_parseEducation(self):
		lines = []
		lines.append('B.E in electronics')
		lines.append('HSC from abc college')
		lines.append('SSC from abc college')
		prDict = {}
		parseEducation(lines, prDict)
		self.assertEqual(1, len(prDict))
		self.assertEqual(1, len(prDict))
		self.assertEqual(True , 'be' in prDict[Attr.value.name])

		lines = []
		lines.append('. B. tech  in electronics')
		lines.append('HSC from abc college')
		lines.append('SSC from abc college')
		prDict = {}
		parseEducation(lines, prDict)
		self.assertEqual(1, len(prDict))
		self.assertEqual(1, len(prDict))
		self.assertEqual(True , 'btech' in prDict[Attr.value.name])

		lines = []
		lines.append('...Bachelor in Arts... From Bangalore')
		lines.append('HSC from abc college in chennai')
		lines.append('SSC from abc college mumbai...')
		prDict = {}
		parseEducation(lines, prDict)
		self.assertEqual(1, len(prDict))
		self.assertEqual(1, len(prDict))
		self.assertEqual(True , 'bachelor' in prDict[Attr.value.name])
		self.assertEqual(True , 'art' in prDict[Attr.value.name])
		

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSectionParseRules)
unittest.TextTestRunner(verbosity=2).run(suite)

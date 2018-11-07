#!/usr/bin/python3.6

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
Prefix = 'Index-'

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
def parseNoop(lineList, prDict):
	pass

#-----------------------------------------------------
# It parses the lines in specified CvSection
# The lines being parsed are expected in below format:
# e.g.: operating systems     :    windows  and unix
# e.g.: core  java, servlets, jsp, jdbc
#
# @param lineList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parseSkill(lineList, prDict):
	skillList = []
	for line in lineList:
		skillList.extend(split_1_then_2(line, ':', ','))

	prDict[Attr.value.name] = Utils.removeDups(skillList)

#-----------------------------------------------------
# It parses the lines in specified CvSection
# Extracts the education details.
# @param lineList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parseEducation(lineList, prDict):
	eduList = []
	for line in lineList:
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
# @param lineList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parseDefault(lineList, prDict):
	emailIdList = []
	phoneList = []
	name = ''
	for line in lineList:

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
#   2. TBD
#
# @param lineList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parsePersonal(lineList, prDict):

	locationList = []

	for line in lineList:

		currLocList = Ref.findLocation(line)
		logger.debug('location:' + str(currLocList))
	
		locationList.extend(currLocList)
	
	prDict[Attr.value.name] = Utils.removeDups(locationList)

#-----------------------------------------------------
# Parses the summary section
#
# @param lineList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parseSummary(lineList, prDict):

	# First matching line with below pattern is picked.
	# Number of years of exprience stored

	for line in lineList:
		re1 = r'(\d{1,2}.\d{0,2}|\d{1,2}\.\d{1,2}).*(year|yr).*(experience)'	
		resultObj = re.search(re1, line, re.I)
		experience = -1
		if (resultObj):
			experience = float(resultObj.group(1))
			break	
	prDict['experience'] = experience

#-----------------------------------------------------
# Parses the speficied lineList
# It assumes the format to be 
#    token1 : value....
#    token2 : value....
#    token3 : value....
#
# @param lineList list of sentences to be parsed.
# @param tokenList conatins token to be matched.
# @param prDict where results will be stored.
# 
#-----------------------------------------------------
def parseTokenValue(lineList, tokenList, prDict):

	currHeader = 'others'
	currValue = ''
	index = len(prDict)
	strIndex  = Prefix + str(index)
	prDict[strIndex] = {}
	for line in lineList:
		wordList = Utils.getWords(line)
		# Skip empty lines
		if (len(wordList) == 0):
			continue
	
		if (wordList[0] in tokenList):

			prDict[strIndex][currHeader] = currValue
			currHeader = wordList[0]
			currValue = ''
			
			# header followed by value on next
			if (len(wordList) == 1):
				continue
			else:
				currValue = ' '.join(wordList[1:])
		else:
			currValue += line + '\n'
	
	prDict[strIndex][currHeader] = currValue


#-----------------------------------------------------
# Parses the Project sections
#
# @param lineList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parseProject(lineList, prDict):

	parseTokenValue(lineList, Ref.PossibleProjectHeader, prDict)

#-----------------------------------------------------
# Parses the Project sections
#
# @param lineList list of sentences to be parsed.
# @param prDict where results will be stored.
#-----------------------------------------------------
def parseWorkHistory(lineList, prDict):

	# ParseOne -- check if it tvFormat?
	# If it has alteast 3 T:V lines, then it said to be tvFormat
	#     e.g.
	#       employer: ibm, pune
	#       role: developer
	#       duration: jan2017 -- till date
	# else
	#   it is not in tvFormat
	#    e.g.
	#       developer at ibm, pune    jan 2017 -- till date

	tempDict = {}
	parseTokenValue(lineList, Ref.PossibleWorkHistoryHeader, tempDict)


	if (len(tempDict[Prefix+ str(0)]) > 2):
		# TODO possible optimization ...can above result be used?
		parseTokenValue(lineList, Ref.PossibleWorkHistoryHeader, prDict)
	else:
		index = len(prDict)
		strIndex  = Prefix + str(index)
		prDict[strIndex] = {}
		for line in lineList:
			prDict[strIndex]['employment'] = line
			index = index + 1
			strIndex  = Prefix + str(index)
			prDict[strIndex] = {}
		

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
		self.assertEqual(True , 'be' in prDict[Attr.value.name])

		lines = []
		lines.append('. B. tech  in electronics')
		lines.append('HSC from abc college')
		lines.append('SSC from abc college')
		prDict = {}
		parseEducation(lines, prDict)
		self.assertEqual(1, len(prDict))
		self.assertEqual(True , 'btech' in prDict[Attr.value.name])

		lines = []
		lines.append('...Bachelor in Arts... From Bangalore')
		lines.append('HSC from abc college in chennai')
		lines.append('SSC from abc college mumbai...')
		prDict = {}
		parseEducation(lines, prDict)
		self.assertEqual(1, len(prDict))
		self.assertEqual(True , 'bachelor' in prDict[Attr.value.name])
		self.assertEqual(True , 'art' in prDict[Attr.value.name])
		
	# ----------- parseSummary ----------
	def test_parseSummary(self):
		lines = []
		lines.append('i have  0.34 years of experience in')
		prDict = {}
		parseSummary(lines, prDict)
		self.assertEqual(1, len(prDict))
		self.assertEqual(0.34, prDict['experience'])

		lines = []
		lines.append('i have  11years of experience in')
		prDict = {}
		parseSummary(lines, prDict)
		self.assertEqual(1, len(prDict))
		self.assertEqual(11, prDict['experience'])

		lines = []
		lines.append('i have  12.55yrs of experience in')
		prDict = {}
		parseSummary(lines, prDict)
		self.assertEqual(1, len(prDict))
		self.assertEqual(12.55, prDict['experience'])

	def test_parseProject(self):

		# Single project
		lines = []
		lines.append('  |project   |enterprise reservations rich|')
		lines.append('|client      |allinclusiveoutlet.com           |')
		lines.append('|duration    |sep-17 to till date.  |')
		lines.append('|team size   |5                   |')
		lines.append('|environment |software |tools&technologies:java, servlets, jsp,     |')
		lines.append('|            |   |html, java script,   |')

		prDict = {}
		parseProject(lines, prDict)
		self.assertEqual(6, len(prDict[0]))
		self.assertEqual('enterprise reservations rich', prDict[0]['project'])

		# Multi project
		prDict = {}

		lines = []
		lines.append('  |project   |enterprise proj1 rich|')
		lines.append('|client      |ibm|')
		lines.append('|duration    |sep-17 to till date.  |')

		parseProject(lines, prDict)
		self.assertEqual(4, len(prDict[0]))
		self.assertEqual('ibm', prDict[0]['client'])

		lines = []
		lines.append('  |project   |enterprise proj2 rich|')
		lines.append('|client      |apple|')
		lines.append('|duration    |sep-18 to till date.  |')
		parseProject(lines, prDict)
		self.assertEqual(4, len(prDict[1]))
		self.assertEqual('apple', prDict[1]['client'])

	def test_parseWorkHistory(self):

		# Single tvFormat
		prDict = {}
		lines = []
		lines.append('|employer |ibm|')
		lines.append('|role |developer|')
		lines.append('|duration |jun2017 -- till date|')

		parseWorkHistory(lines, prDict)
		self.assertEqual(4, len(prDict[0]))
		self.assertEqual('ibm', prDict[0]['employer'])

		# Multi tvFormat
		prDict = {}
		lines = []
		lines.append('|employer |ibm|')
		lines.append('|role |developer|')
		lines.append('|duration |jun2017 -- till date|')
		parseWorkHistory(lines, prDict)

		lines = []
		lines.append('|employer |fiserv|')
		lines.append('|role |developer|')
		lines.append('|duration |jun2015 -- jun2017|')
		parseWorkHistory(lines, prDict)

		self.assertEqual(4, len(prDict[1]))
		self.assertEqual('fiserv', prDict[1]['employer'])

		# Single non-tvFormat
		prDict = {}
		lines = []
		lines.append('ibm  developer jun2017 -- till date')
		lines.append('fiserv  developer jun2015 -- jun2017')

		parseWorkHistory(lines, prDict)

		self.assertEqual(1, len(prDict[0]))
		self.assertEqual(1, len(prDict[1]))
		self.assertEqual('ibm  developer jun2017 -- till date', prDict[0]['employment'])
		self.assertEqual('fiserv  developer jun2015 -- jun2017', prDict[1]['employment'])


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSectionParseRules)
unittest.TextTestRunner(verbosity=2).run(suite)


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSectionParseRules)
unittest.TextTestRunner(verbosity=2).run(suite)

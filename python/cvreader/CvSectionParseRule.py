#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')

from common.Utils import *
from CvSections import *
from CvParseRule import *

def split_1_then_2(line, splitChar1, splitChar2):
	firstSplitToks = line.split(splitChar1)

	# Doesnt have splitChar1
	if (len(firstSplitToks) == 1):
		return firstSplitToks[0].split(splitChar2)

	# Has splitChar1
	return firstSplitToks[1].split(splitChar2)
	

#-----------------------------------------------------
# It parses the lines in specified CvSection
# The lines being parsed are expected in below format:
# e.g.: operating systems     :    windows  and unix
# e.g.: core  java, servlets, jsp, jdbc
#
# @param CvSection containing the lines to be parsed.
# NOTE : It modifies the input object.
#-----------------------------------------------------
def parseSkill(cvSec):
	skillList = []
	for line in cvSec.getLineList():
		skillList.extend(split_1_then_2(line, ':', ','))

	cvSec.addParseResult(Section.skill.name, skillList)

#-----------------------------------------------------
# It parses the lines in specified CvSection
# Logic:
#   1. It extracts email
#   2. It extracts phone
#   3. If above extraction has no results
#      it assumes this line to be name.
#
# @param CvSection containing the lines to be parsed.
# NOTE : It modifies the input object.
#-----------------------------------------------------
def parseDefault(cvSec):
	emailIdList = []
	phoneList = []
	name = ''
	for line in cvSec.getLineList():

		# Extract email
		if (len(emailIdList) == 0):
			emailIdList = CvParseRule.getEmail(line)

		if (len(phoneList) == 0):
			phoneList = CvParseRule.getPhone(line)

		
		if ((len(emailIdList) == 0) and (len(phoneList) == 0)):
			name = line

	# Remove tags from name
	name = split_1_then_2(name, ':', '__anything__')[0].strip()

	cvSec.addParseResult('emailid', emailIdList)
	cvSec.addParseResult('phone', phoneList)
	cvSec.addParseResult('name',  name)

#-----------------------------------------------------
# It parses the lines in specified CvSection
# Logic:
#   1. It extracts location
#   2. It extracts DOB
#
# @param CvSection containing the lines to be parsed.
# NOTE : It modifies the input object.
#-----------------------------------------------------
def parsePersonal(cvSec):
	location = ''
	dob = ''
	married = ''

#------------------------------------------
# Unit test
#------------------------------------------
class TestThisClass(unittest.TestCase):

	# ----------- parseSkill ----------
	def test_parseSkill_with_colon(self):

		cvSec = CvSection(Section.skill.name, ['skill'])

		lines = []
		lines.append('operating systems     :    windows  and unix')
		lines.append('j2ee  technologies    :    core  java, servlets, jsp, jdbc')
		lines.append('frameworks   /methodologies   :    spring,   hibernate')

		for line in lines:
			cvSec.addLine(line)

		parseSkill(cvSec)

		self.assertEqual(1, len(cvSec.getParseResult()))
		self.assertEqual(7, len(cvSec.getParseResult()[Section.skill.name]))

	# ----------- parseSkill ----------
	def test_parseSkill_nocolon(self):

		cvSec = CvSection(Section.skill.name, ['skill'])

		lines = []
		lines.append('windows  and unix')
		lines.append('core  java, servlets, jsp, jdbc')
		lines.append('spring,   hibernate')

		for line in lines:
			cvSec.addLine(line)

		parseSkill(cvSec)

		self.assertEqual(1, len(cvSec.getParseResult()))
		self.assertEqual(7, len(cvSec.getParseResult()[Section.skill.name]))

	# ----------- parseDefault ----------
	def test_parseDefault(self):

		cvSec = CvSection(Section.default.name, [''])

		lines = []
		lines.append('name : First Last')
		lines.append('email : first.last@gmail.com')
		lines.append('mobile : +91 1112223344, 2223334455')

		for line in lines:
			cvSec.addLine(line)

		parseDefault(cvSec)
		self.assertEqual(3, len(cvSec.getParseResult()))
		self.assertEqual('first.last@gmail.com', cvSec.getParseResult()['emailid'][0])
		#self.assertEqual('+91 1112223344', cvSec.getParseResult()['phone'][0])
		self.assertEqual('First Last', cvSec.getParseResult()['name'])

	# ----------- parseDefault ----------
	def test_parseDefault_wo_token(self):

		cvSec = CvSection(Section.default.name, [''])

		lines = []
		lines.append('First Last')
		lines.append('first.last@gmail.com')
		lines.append('+91 1112223344, 2223334455')

		for line in lines:
			cvSec.addLine(line)

		parseDefault(cvSec)
		self.assertEqual(3, len(cvSec.getParseResult()))
		self.assertEqual('first.last@gmail.com', cvSec.getParseResult()['emailid'][0])
		#self.assertEqual('+91 1112223344', cvSec.getParseResult()['phone'][0])
		self.assertEqual('First Last', cvSec.getParseResult()['name'])

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestThisClass)
unittest.TextTestRunner(verbosity=2).run(suite)

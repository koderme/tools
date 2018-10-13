#!/usr/bin/python3.5

import os
import re
import unittest
import sys
sys.path.append('..')

from ReferenceData import *
from common.Utils import *
from nltk.tokenize import sent_tokenize, word_tokenize


#---------------------------------------------------
# CvParseRule maintains collections of rules used for
# detecting
#     > SectionHeader
#     > SectionBody
#     > Others
# 
#---------------------------------------------------

class CvParseRule:
	# Identify line
	def getLineType(line):
		wordList = Common.wordTokenize(line)
		retType = Ref.LineType.Others.name
		wLen = len(wordList)

		if (wLen == 0):
			retType = Ref.LineType.Others.name
		elif ((wLen >= 1) and (wLen <= 3)):
			retType = Ref.LineType.SectionHeader.name
		else:
			retType = Ref.LineType.SectionBody.name

		return retType

	#------------------------------------------
	# Extracts all email id from the line.
	# E.g 'hello test@gmail.com john@outlook.com'
	#   would return [test@gmail.com, john@outlook.com'
	#------------------------------------------
	def getEmail(line):
		emailList = re.findall('\S+@\S+', line) 
		return emailList

	def getPhone(line):
		regEx = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
		phoneList = re.findall(regEx, line)
		#print(str(phoneList))
		return phoneList

#------------------------------------------
# Unit test
#------------------------------------------
class TestCvParseRule(unittest.TestCase):

	def test_SectionHeader(self):
		# 
		line = 'summary'
		self.assertEqual(Ref.LineType.SectionHeader.name, CvParseRule.getLineType(line))
		# 
		line = 'work history'
		self.assertEqual(Ref.LineType.SectionHeader.name, CvParseRule.getLineType(line))
		# 
		line = 'xxx YYY zzZ:'
		self.assertEqual(Ref.LineType.SectionHeader.name, CvParseRule.getLineType(line))

	def test_SectionBody(self):

		# 
		line = 'Experience with java, spring'
		self.assertEqual(Ref.LineType.SectionBody.name, CvParseRule.getLineType(line))
		# 
		line = 'Certified in AWS archtecture....and aws networking'
		self.assertEqual(Ref.LineType.SectionBody.name, CvParseRule.getLineType(line))

	def test_Others(self):
		# 
		line = ':'
		self.assertEqual(Ref.LineType.Others.name, CvParseRule.getLineType(line))
		# 
		line = ':::  '
		self.assertEqual(Ref.LineType.Others.name, CvParseRule.getLineType(line))

	def test_extractEmail(self):
		# 
		line = 'email: test@gmail.com alternate-email test2@outlook.com '
		emailList = CvParseRule.getEmail(line)
		self.assertEqual(2, len(emailList))
		self.assertEqual('test@gmail.com', emailList[0])
		self.assertEqual('test2@outlook.com', emailList[1])

		# 
		line = 'email: @gmail.com alternate-email test2@outlook.com something@ '
		emailList = CvParseRule.getEmail(line)
		self.assertEqual(1, len(emailList))
		self.assertEqual('test2@outlook.com', emailList[0])

		# 
		line = 'email: @gmail.com alternate-email @outlook.com something@ '
		emailList = CvParseRule.getEmail(line)
		self.assertEqual(0, len(emailList))

	def test_extractPhone(self):
		# 
		line = 'ph no       : +916300153913'
		phoneList = CvParseRule.getPhone(line)
		line = 'email: monika.arya0118@gmail.com phone: +91-7767900443'
		phoneList = CvParseRule.getPhone(line)
		line = 'snehal auti      phone: (+91) 83-7899-0878'
		phoneList = CvParseRule.getPhone(line)
		line = ' phone: +91- 9721695547'
		phoneList = CvParseRule.getPhone(line)
		line = 'ph no       : +916300153913'
		phoneList = CvParseRule.getPhone(line)
		line = 'venkata subbaraju rallabandi                              phone: 9676018342'
		phoneList = CvParseRule.getPhone(line)
		line = ':email id: sharvila.gawande@gmail.com                                           phone no: +91-9096080922'
		phoneList = CvParseRule.getPhone(line)
		self.assertEqual(1, len(phoneList))

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvParseRule)
unittest.TextTestRunner(verbosity=2).run(suite)

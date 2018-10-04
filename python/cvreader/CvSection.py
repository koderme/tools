#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')

from common.Utils import *


CvTag =  Enum('', 'summary skill role project employer certification personal')

#---------------------------------------------------
# CvSection represents 1 section of Cv.
# It stores following metadata
#    secName  --> name of the section
#    secTags  --> If matching tag is found, it 
#                 indicates start of section
#    parseLogic --> Function that would be executed
#                   for parsing <sentences>
#    secTagNameDict --> temp dictionary that 
#                       store <SecTag> Vs <SecName>
#---------------------------------------------------

class CvSection:
	def __init__(self, secName, secTags, parseLogic):
		self.secName = secName
		self.secTags = secTags
		self.parseLogic = parseLogic
		self.sentenceList = []
		self.setSecTagNameDict()

	def setSecTagNameDict(self):
		self.secTagNameDict = {}
		for secTag in self.secTags:
			self.secTagNameDict[secTag] = self.secName

	def getSecName(self):
		return self.secName

	def getSecTagNameDict(self):
		return self.secTagNameDict

	def getSentences(self):
		return self.sentenceList

	def addSentence(self, sentence):
		self.sentenceList.append(sentence)

	def parse(self):
		for sentence in self.sentenceList:
			logging.info('parsing :' + sentence)


class TestCvSection(unittest.TestCase):

	def test_constructor(self):
		# Unique tags
		cvSection = CvSection('sec1', ['tag1', 'tag101'], 'some-func')
		self.assertEqual(2, len(cvSection.getSecTagNameDict()))

		# Non-Unique tags
		cvSection = CvSection('sec2', ['tag22', 'tag22'], 'some-func')
		self.assertEqual(1, len(cvSection.getSecTagNameDict()))

	def test_addSentence(self):
		cvSection = CvSection('sec1', ['tag1', 'tag101'], 'some-func')

		sentence1 = 'this is a test line 1'
		cvSection.addSentence(sentence1)
		self.assertEqual(sentence1, cvSection.getSentences()[0])
		self.assertEqual(1, len(cvSection.getSentences()))

		sentence2 = 'this is a test line 2'
		cvSection.addSentence(sentence2)
		self.assertEqual(sentence2, cvSection.getSentences()[1])

		self.assertEqual(2, len(cvSection.getSentences()))

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSection)
unittest.TextTestRunner(verbosity=2).run(suite)

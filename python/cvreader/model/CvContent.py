#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from Common import *
from model.ReferenceData import *


#-------------------------------------------------------------
# CvContent is a dictionary of
#    section-name Vs sentence[]
#-------------------------------------------------------------
class CvContent:
	def __init__(self):
		self.contentDict = {}

	def add(self, sectionName, sentence):
		sentenceList = self.contentDict.get(sectionName)
		if (sentenceList == None):
			sentenceList = []
			self.contentDict[sectionName] = sentenceList
		sentenceList.append(sentence)

	def getSentenceList(self, sectionName):
		sentenceList = self.contentDict.get(sectionName)
		if (sentenceList == None):
			return []
		return sentenceList	

	def getContentDict(self):
		return self.contentDict

#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestCvContent(unittest.TestCase):

	def test_get_sentence(self):

		content = CvContent()

		content.add(Ref.Section.personal.name, 'email: test@gmail.com')
		content.add(Ref.Section.personal.name, 'name: John White')

		sentList = content.getSentenceList(Ref.Section.personal.name)
		self.assertEqual(2, len(sentList))

		content.add(Ref.Section.skill.name, 'java cpp python')
		sentList = content.getSentenceList(Ref.Section.skill.name)
		self.assertEqual(1, len(sentList))

		sentList = content.getSentenceList(Ref.Section.unknown.name)
		self.assertEqual(0, len(sentList))



# Run unit tests
#if __name__ == '__main__':
#unittest.main()
logging.basicConfig(level=logging.INFO)
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvContent)
unittest.TextTestRunner(verbosity=2).run(suite)

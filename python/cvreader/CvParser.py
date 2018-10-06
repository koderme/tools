#!/usr/bin/python3.5

import os
from nltk.tokenize import sent_tokenize, word_tokenize

import sys
sys.path.append('..')

from common.Utils import *
from CvSections import *


FIELD_SEP = ','



#----------------------------------------------------
# CvParser functions to parse the CV.
#
# Note:
# * CV consists of multiple section.
# * CvSection starts when tags defined in CvSection are found.
# * CvSection ends another Section starts.
#
#----------------------------------------------------
class CvParser:
	def __init__(self, inFilepath):
		self.inFilepath = inFilepath
		self.cvSections = CvSections()

	def getText(self):
		str1 = open(self.inFilepath, 'r').read()
		return str1

	def parse(self):
		str1 = self.getText()
		sentenceList = sent_tokenize(str1)
		self.cvSections.parse(sentenceList)
		self.cvSections.show()
	
#----------------------------------------------------
# Generates report with specified skills
#----------------------------------------------------
def findMatchingCv2(inDir, skillArr):
	for root, _, fileArr in os.walk(inDir):
		for rFile in fileArr: 
			fpath = os.path.join(root, rFile)

			if ( rFile.endswith(".txt")):
				stringCV = parseFile(fpath)
			else:
				logging.info("unknwo extn...skipping")
#----------------------------------------------------
# Main
#----------------------------------------------------
logging.basicConfig(level=logging.INFO)
cvParser = CvParser('cv.txt')
cvParser.parse()



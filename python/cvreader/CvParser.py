#!/usr/bin/python3.5

import docx
import os
import textract
from docx import Document

from SkillSet import *

import sys
sys.path.append('..')
from common.Utils import *
from Constants import *

# This tool is expected to scan the document, convert into below format
# name       |source | req        |rating| <s> | <s> | <s> | ... | match
# John White |naukri | java-spring| 3S   | 1   | 1   | 0   |     | <sum>
#

State = Enum('', 'processed errored')
Tags = Enum('', 'srcfile content retcode')

FIELD_SEP = ','

#----------------------------------------
# Generates report with specified skills
#----------------------------------------
def findMatchingCv(inDir, skillArr):
	colHead = [ 'date', 'src', 'fpath' ] + ALL_FIELDS + [ 'match']
	print(FIELD_SEP.join(colHead))
	for root, _, fileArr in os.walk(inDir):
		for rFile in fileArr: 
			fpath = os.path.join(root, rFile)
			fpathSplitted = fpath.split('/')

			# retain last 3
			l2 = fpathSplitted[-3:]
			result = FIELD_SEP.join(l2)
			
			skillMatchCount = 0	
			if ( rFile.endswith("docx") or rFile.endswith('doc') or rFile.endswith('pdf') ):

				stringCV = parseFile(fpath)
				for skill in skillArr:
					if (stringCV.find(skill) != -1):
						result += FIELD_SEP + '1';
						skillMatchCount += 1
					else:
						result += FIELD_SEP + '0';

				# Extract experience
				index = stringCV.find('year')
				
			result += FIELD_SEP + str(skillMatchCount)
			print(result)


#----------------------------------------
#----------------------------------------
class CvMatcher:
	def __init__(self, inFilepath):
		self.inFilepath = inFilepath
		logging.info('xxxx:' + self.inFilepath + ':')
		self.setDirs()
	
#----------------------------------------
# Main
#----------------------------------------
#logging.basicConfig(level=logging.INFO)
#dir1='temp'
#CvConverter.convertToText(dir1)



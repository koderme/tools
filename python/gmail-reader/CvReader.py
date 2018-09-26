#!/usr/bin/python3.5

import docx
import os
import textract

from docx import Document
from SkillSet import *


# This tool is expected to scan the document, convert into below format
# name       |source | req        |rating| <s> | <s> | <s> | ... | match
# John White |naukri | java-spring| 3S   | 1   | 1   | 0   |     | <sum>
#

FIELD_SEP = ','


def parseDocx(filename):
	doc = docx.Document(filename)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.text)
	return '\n'.join(fullText).lower()

def parseFile(inFile):
	try:
		#return textract.process(inFile).decode('utf-8').lower()
		return textract.process(inFile).decode().lower()
	except:
		print("Error extracting text from (%s)" % (inFile)) 
		return ''

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


dir1='downloads/20180925'
findMatchingCv(dir1, ALL_FIELDS)



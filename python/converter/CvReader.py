#!/usr/bin/python3.5

import docx
import os
import textract

from docx import Document


# This tool is expected to scan the document, convert into below format
# name       |source | req        |rating| <s> | <s> | <s> | ... | match
# John White |naukri | java-spring| 3S   | 1   | 1   | 0   |     | <sum>
#

LOCATION         = [ 'bengaluru', 'banglore', 'mumbai', 'hyderabad', 'chennai', 'gurgaon', 'noida' ]
JAVA_BACKEND     = [ 'java', 'spring', 'j2ee' ]
JAVA_WEBSERVICES = [ 'soap', 'rest', 'webservices' ]
JAVA_CLOUD       = [ 'spring boot', 'cloud', 'microservices' ]
CLOUD_FRAMEWORK  = [ 'aws', 'azure', 'google' ]
SCRIPTING        = [ 'python', 'ksh', 'bash', 'perl' ]
ARCHITECT        = [ 'design pattern', 'architect']
OS               = [ 'windows', 'ios', 'android', 'unix']
UI               = [ 'angular', 'jsp', 'node.js', 'jquery' ]
CERTIFICATION    = [ 'certification' ]
DOT_NET_MATCH_SKILL = [ 'php', 'net', 'c#', 'asp.net', 'windows' ]
DB               = [ 'db2', 'oracle', 'msqsql', 'mysql', 'plsql', 'pl/sql' ]
ORM              = [ 'jpa', 'hibernate' ]
INTEGRATION      = [ 'mq', 'kafka' ]
BUILD            = [ 'maven', 'ant', 'teamcity' ]
CONTAINER        = [ 'docker', 'puppet', 'chef', 'ansible' ]
OTHERS           = [ 'bluetooth', 'gaming', 'embedded' ]

ALL_FIELDS =  LOCATION + JAVA_BACKEND + JAVA_WEBSERVICES + JAVA_CLOUD + CLOUD_FRAMEWORK + SCRIPTING + ARCHITECT + OS + UI + CERTIFICATION + DOT_NET_MATCH_SKILL + DB + ORM + INTEGRATION + BUILD + CONTAINER + OTHERS

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
	colHead = [ 'src', 'req', 'rating', 'fpath' ] + ALL_FIELDS + [ 'match']
	print(FIELD_SEP.join(colHead))
	for root, _, fileArr in os.walk(inDir):
		for rFile in fileArr: 
			fpath = os.path.join(root, rFile)
			fpathSplitted = fpath.split('/')
			fpathSplitted.pop(0)  # Remove first token
			result = FIELD_SEP.join(fpathSplitted)

			if ( rFile.endswith("docx") or rFile.endswith('doc') or rFile.endswith('pdf') ):

				stringCV = parseFile(fpath)
				skillMatchCount = 0	
				for skill in skillArr:
					if (stringCV.find(skill) != -1):
						result += FIELD_SEP + '1';
						skillMatchCount += 1
					else:
						result += FIELD_SEP + '0';
			result += FIELD_SEP + str(skillMatchCount)
			print(result)


dir1='downloads'
findMatchingCv(dir1, ALL_FIELDS)



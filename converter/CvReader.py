#!/usr/bin/python3.5

import docx
import os

from docx import Document


# This tool is expected to scan the document, convert into below format
# name       |source | req        |rating| <s> | <s> | <s> | ... | match
# John White |naukri | java-spring| 3S   | 1   | 1   | 0   |     | <sum>
#

JAVA_BACKEND     = [ 'java', 'spring', 'j2ee' ]
JAVA_WEBSERVICES = [ 'soap', 'rest', 'webservices' ]
JAVA_CLOUD       = [ 'spring boot', 'cloud', 'microservices' ]
CLOUD_FRAMEWORK  = [ 'aws', 'azure', 'google' ]
SCRIPTING        = [ 'python', 'ksh', 'bash', 'perl' ]
ARCHITECT        = [ 'design pattern', 'architect']
OS               = [ 'windows', 'ios', 'android', 'unix']
CERTIFICATION    = [ 'certification' ]
DOT_NET_MATCH_SKILL = [ 'php', 'net', 'c#', 'asp.net', 'windows' ]
DB               = [ 'db2', 'oracle', 'msqsql', 'mysql', 'plsql', 'pl/sql' ]
ORM              = [ 'jpa', 'hibernate' ]
INTEGRATION      = [ 'mq', 'kafka' ]
BUILD            = [ 'maven', 'ant', 'teamcity' ]
CONTAINER        = [ 'docker', 'puppet', 'chef', 'ansible' ]
OTHERS           = [ 'bluetooth', 'gaming', 'embedded' ]

ALL =  JAVA_BACKEND + JAVA_WEBSERVICES + JAVA_CLOUD + CLOUD_FRAMEWORK + SCRIPTING + ARCHITECT + OS + CERTIFICATION + DOT_NET_MATCH_SKILL + DB + ORM + INTEGRATION + BUILD + CONTAINER + OTHERS

FIELD_SEP = ','



def parseDocx(filename):
	doc = docx.Document(filename)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.text)
	return '\n'.join(fullText)


def findMatchingCv(inDir, skillArr):
	for root, _, filenames in os.walk(inDir):
		for filename in filenames: 
			print("---------------------------")

			fpath = os.path.join(root,filename)
			fpathSplitted = fpath.split('/')
			fpathSplitted.pop(0)  # Remove first token
			result = FIELD_SEP.join(fpathSplitted)

			if (filename.endswith("docx")):

				stringCV = parseDocx(fpath)
			
				for skill in skillArr:
					if (stringCV.find(skill) != -1):
						result += FIELD_SEP + '1';
					else:
						result += FIELD_SEP + '0';
			print(result)


dir1='downloads'
findMatchingCv(dir1, ALL)



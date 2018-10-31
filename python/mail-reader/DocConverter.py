#!/usr/bin/python3.6

import docx
import os
import textract
from docx import Document

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
# Extracts text from docx
#----------------------------------------
def extractTextFromDocx(inFilepath):
	doc = docx.Document(inFilepath)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.content)
	return '\n'.join(fullText).lower()

#----------------------------------------
# Returns output text filepath. 
# The name is derived as follows:
#   prefix + extn 
#     prefix = content of inPath with [0]th token replaced with 'processed'
#     suffix = orig suffix replaced with 'txt'
#----------------------------------------
def getOuputTextFilename(inFilepath):
	outFilepath = Utils.nameWithoutExtn(inFilepath) + '.txt'
	toks = outFilepath.split('/')
	toks[0] = State.processed.name
	return '/'.join(toks)


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
class DocConverter:
	def __init__(self, inFilepath):
		self.inFilepath = inFilepath
		logging.info('xxxx:' + self.inFilepath + ':')
		self.setDirs()
	
	#----------------------------------------
	# Returns dict with corr's entries for 
	#  processed, errrored dirs
	#----------------------------------------
	def setDirs(self):
		toks = self.inFilepath.split('/')
		del toks[len(toks)-1]

		toks[0] = State.processed.name
		self.processedDir = '/'.join(toks)

		toks[0] = State.errored.name
		self.erroredDir = '/'.join(toks)

	#----------------------------------------
	# Extracts text from docx/doc/pdf
	#----------------------------------------
	def extract(self):
		logging.info('parsing ...')
		content = ''
		retcode = RC_CODE.ERROR.name
		try:
			content = textract.process(self.inFilepath).decode().lower()
			retcode = RC_CODE.OK.name
		except:
			content = "Error extracting content from (%s)" % (self.inFilepath),

		self.content = content
		self.retcode = retcode
		logging.info('parsing result : ' + retcode)

	#----------------------------------------
	# Does the post processing
	#  moving orig file to processed-dir / errored-dir
	#  creating text file in processed-dir 
	#----------------------------------------
	def postProcess(self):
		logging.debug('retcode:' + self.retcode)
		if self.retcode == RC_CODE.OK.name:
			Utils.move(self.inFilepath, self.processedDir)

			self.outFilepath = getOuputTextFilename(self.inFilepath)
			logging.info('writing content to ' + self.outFilepath)
			f = open(self.outFilepath, "w+")
			f.write(self.content)
			f.close()
		else:
			Utils.move(self.inFilepath, self.erroredDir)

	#----------------------------------------
	# Validates the extension
	#----------------------------------------
	def isValid(inFilepath):
		# Check existence
		logging.info('xxxx:' + inFilepath + ':')
		if not os.path.isfile(inFilepath):
			logging.error("Invalid in file :" + inFilepath)
			return False

		if os.path.isdir(inFilepath):
			logging.error("Is a dir :" + inFilepath)
			return False

		if ( inFilepath.endswith("docx") or
				inFilepath.endswith('doc') or
				inFilepath.endswith('pdf') ):
			return True
		else:
			return False
	
#----------------------------------------
# Converts files from pdf/docx/doc to text
#----------------------------------------
	def convertToText(inDir):
		if not os.path.isdir(inDir):
			logging.error("Invalid dir :" + inDir)
			exit

		summary =  {'valid' : 0, 'invalid' : 0}
		for root, _, fileArr in os.walk(inDir):
			for rFile in fileArr: 

				#Utils.sleep(1000)

				logging.info('------------------------------')
				logging.info('processing : ' + rFile)
				fpath = os.path.join(root, rFile)

				if ( DocConverter.isValid(fpath)):
					summary['valid'] += 1;
					cvParser = DocConverter(fpath) 
					cvParser.extract()
					cvParser.postProcess()
				else:
					summary['invalid'] += 1;
					logging.warn('unknown extension :' + rFile + ' skipping ...')

		logging.info('summary:' + str(summary))
			

#----------------------------------------
# Main
#----------------------------------------
#logging.basicConfig(level=logging.INFO)
#dir1='temp'
#DocConverter.convertToText(dir1)



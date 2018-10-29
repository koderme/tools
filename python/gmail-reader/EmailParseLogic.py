#!/usr/bin/python3.6

import sys
import os

sys.path.append('..')

from interface import implements, Interface
from common.Utils import *
from Constants import *



IGNORE_WORDS_IN_SUBJECT = [ 'fwd:', 'star', '3', '4', '5', 'opening', 'for', 'applicant', '-', 'naukri.com', 'hirist', 'yrs', 'years', 'forward', '/']
NOW_YYYMMDD = Utils.currentDate()

#-------------------------------------------
# Email parser
#-------------------------------------------

class EmailParseLogic:

	@staticmethod
	def parseSubject(subjectStr):
	
		attrs = {
			'source' : CV_SOURCE.others.name,
			'rating' : 'not-rated',
			'req'    : 'none',
		}

		if ( subjectStr.find(CV_SOURCE.naukri.name) != -1):
			attrs = parseSubjectNaukri(subjectStr)
		elif ( subjectStr.find(CV_SOURCE.hirist.name) != -1):
			attrs['source'] = CV_SOURCE.hirist.name

		return attrs

	@staticmethod
	def parseBody(bodyStr):
		print('test')


	@staticmethod
	def getSenderName(message):
		senderToks = message['from'].split();
		senderToks.pop(-1)
		return '.'.join(senderToks)

	@staticmethod
	def getSenderEmail(message):
		sender = message['from'].split()[-1]
		s1 = sender.replace("<", "").replace(">", "")
		return s1

	@staticmethod
	def downloadAttachment(part, emailMesg):
		subAttr = EmailParseLogic.parseSubject(emailMesg.subject)
	
		toks = [DIRS.DOWNLOAD_DIR , NOW_YYYMMDD,  subAttr['source'] ]
		downloadDir = '/'.join(toks)
		Utils.createDir(downloadDir)	

		origFileName_ = part.get_filename()
		if bool(origFileName_):
			origFileName = origFileName_.lower()

			# Skip images
			if (not (origFileName.endswith(FILE_EXTN.DOC) or
				origFileName.endswith(FILE_EXTN.DOCX) or
				origFileName.endswith(FILE_EXTN.PDF))):
				logging.info('...skipping attachment other than pdf/doc*')
				return

			fileName = emailMesg.senderName + '-' + NOW_YYYMMDD + '-' + origFileName
			filePath = os.path.join(downloadDir, fileName)
			if not os.path.isfile(filePath) :
				logging.info('...downloading attachment : %s', origFileName)
				fp = open(filePath, 'wb')
				fp.write(part.get_payload(decode=True))
				fp.close()
			else:
				logging.error('error: file(%s) already exist' % (fileName))


#-------------------------------------------
# Naukri subject parser
#-------------------------------------------
def parseSubjectNaukri(subjectStr):

	logging.debug('parseSubjectNaukri()')
	attrs = {
		'source' : CV_SOURCE.naukri.name,
		'rating' : 'not-rated',
		'req'    : 'none',
	}

	if ( subjectStr.find(NAUKRI_RATING.S2) != -1):
		attrs['rating'] = NAUKRI_RATING.S2
	elif ( subjectStr.find(NAUKRI_RATING.S3) != -1):
		attrs['rating'] = NAUKRI_RATING.S3
	elif ( subjectStr.find(NAUKRI_RATING.S4) != -1):
		attrs['rating'] = NAUKRI_RATING.S4
	elif ( subjectStr.find(NAUKRI_RATING.S5) != -1):
		attrs['rating'] = NAUKRI_RATING.S5

	# Requirement
	attrs['req'] = parseSubjectRequirement(subjectStr)

	return attrs

#-------------------------------------------
# Naukri subject parser
#-------------------------------------------
def parseSubjectRequirement(subject_):

	subjectStr = subject_.replace('/', '-')
	
	# Naukri format of subjectStr
	# 3 star applicant - Naukri.com - Opening for Java Spring Hibernate Developer - Member Technical Staff, Metric Stream Infotech, 2.6 yrs, Bengaluru / Bangalore
	#
	toks = 'req-unknown'.split()
	if (subjectStr.find(CV_SOURCE.naukri.name) != -1):
		subjectToks = subjectStr.split('-')
		if (len(subjectToks) >= 3):
			toks = subjectToks[2].split()

	x = [i for i in toks if i not in IGNORE_WORDS_IN_SUBJECT] 
	return '-'.join(x)

#-------------------------------------------
# Naukri body parser
#-------------------------------------------
def parseBodyNaukri(rawStr):
	print('test')

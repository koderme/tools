#!/usr/bin/python3.5
#
# Very basic example of using Python 3 and IMAP to iterate over emails in a
# gmail folder/label.  This code is released into the public domain.
#
# This script is example code from this blog post:
# http://www.voidynullness.net/blog/2013/07/25/gmail-email-with-python-via-imap/
#
# This is an updated version of the original -- modified to work with Python 3.4.
#
import sys
sys.path.append('..')

import imaplib
import getpass
import email
import email.header
import os
import logging

from common.Util import *

# Dir structure
# <source>/<req>/<rating>/<sender>-<yyyymmdd>-<actual-filename>
#


#----------------------------------------
# Constants
#----------------------------------------
NOW_YYYMMDD = currentDate()
WORK_DIR = currentDate()

EMAIL_ACCOUNT = "sales.hueklr@gmail.com"
EMAIL_ACCOUNT = "cv.hueklr@gmail.com"

# Use 'INBOX' to read inbox.  Note that whatever folder is specified, 
# after successfully running this script all emails in that folder 
# will be marked as read.
EMAIL_FOLDER = "INBOX"

EMAIL_CATEGORY = 'ALL'
EMAIL_CATEGORY = '(UNSEEN)'

RESUME_SRC_HIRIST = 'hirist'
RESUME_SRC_NAUKRI = 'naukri'
RESUME_SRC_OTHERS = 'others'

NAUKRI_RATING_2_STAR = '2 star applicant'
NAUKRI_RATING_3_STAR = '3 star applicant'
NAUKRI_RATING_4_STAR = '4 star applicant'
NAUKRI_RATING_5_STAR = '5 star applicant'

RC_OK = 'OK'

#----------------------------------------
# setup
#----------------------------------------
def setup():
	logging.basicConfig(level=logging.INFO)
	NOW_YYYMMDD = currentDate()

def process_mailbox(M):

	"""
	Do something with emails messages in the folder.  
	For the sake of this example, print some headers.
	"""

	retCode, emailArr = M.search(None, EMAIL_CATEGORY)
	if retCode != RC_OK:
		logging.info("No messages found!")
		return

	for msgId in emailArr[0].split():

		retCode, fetchedEmail = M.fetch(msgId, '(RFC822)')
		if retCode != RC_OK:
			logging.error("ERROR getting message", msgId)
			return

		msg = email.message_from_bytes(fetchedEmail[0][1])

		# Email details
		hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
		subject = str(hdr).lower()
		senderName = getSenderName(msg)
		senderEmail = getSenderEmail(msg)
		downloadDir = parseSubject(subject)	
		createDir(downloadDir)	

		for part in msg.walk():
			logging.debug(dir(part))
			if part.get_content_maintype() == 'multipart':
				logging.debug(part.as_string())
				continue
			if part.get('Content-Disposition') is None:
				logging.debug(part.as_string())
				continue
			origFileName_ = part.get_filename()
			if bool(origFileName_):
				origFileName = origFileName_.lower()
				# Skip images
				if (origFileName.endswith('jpeg') or origFileName.endswith('jpg') or origFileName.endswith('png')):
					continue
				logging.info('message with attachment %s', origFileName)
				fileName = senderName + '-' + NOW_YYYMMDD + '-' + origFileName
				filePath = os.path.join(downloadDir, fileName)
				if not os.path.isfile(filePath) :
					logging.info(fileName)
					fp = open(filePath, 'wb')
					fp.write(part.get_payload(decode=True))
					fp.close()
				else:
					logging.error('error: file(%s) already exist' % (fileName))

		logging.info('----------------------------------------------------');
		logging.info('Message %s: %s' % (msgId, subject))
		logging.info('Raw Date: %s' % (msg['Date']))

		# Now convert to local date-time
		date_tuple = email.utils.parsedate_tz(msg['Date'])
		if date_tuple:
			local_date = datetime.datetime.fromtimestamp(
				email.utils.mktime_tz(date_tuple))
			logging.info("Local Date: " + local_date.strftime("%a, %d %b %Y %H:%M:%S"))

def getSenderName(message):
	senderToks = message['from'].split();
	senderToks.pop(-1)
	return '.'.join(senderToks)

def getSenderEmail(message):
	sender = message['from'].split()[-1]
	return sender.replace('<', '').replace('>', '')

def parseSubjectRequirement(subject_):

	subject = subject_.replace('/', '-')
	IGNORE_WORDS = [ 'fwd:', 'star', '3', '4', '5', 'opening', 'for', 'applicant', '-', 'naukri.com', 'hirist', 'yrs', 'years', 'forward', '/']
	
	# Naukri format of subject
	# 3 star applicant - Naukri.com - Opening for Java Spring Hibernate Developer - Member Technical Staff, Metric Stream Infotech, 2.6 yrs, Bengaluru / Bangalore
	#
	toks = 'req-unknown'.split()
	if (subject.find(RESUME_SRC_NAUKRI) != -1):
		subjectToks = subject.split('-')
		if (len(subjectToks) >= 3):
			toks = subjectToks[2].split()
	elif (subject.find(RESUME_SRC_HIRIST) != -1):
		subjectToks = subject.split('-')
		if (len(subjectToks) >= 2):
			toks = subjectToks[1].split()

	x = [i for i in toks if i not in IGNORE_WORDS] 
	return '-'.join(x)

def parseSubject(subject):

	source = RESUME_SRC_OTHERS

	# Rating
	rating = 'not-rated'

	if (subject.find(RESUME_SRC_HIRIST) != -1):
		source = RESUME_SRC_HIRIST
	elif ( subject.find(RESUME_SRC_NAUKRI) != -1):
		source = RESUME_SRC_NAUKRI
		if ( subject.find(NAUKRI_RATING_2_STAR) != -1):
			rating = '2STAR'
		elif ( subject.find(NAUKRI_RATING_3_STAR) != -1):
			rating = '3STAR'
		elif ( subject.find(NAUKRI_RATING_4_STAR) != -1):
			rating = '4STAR'
		elif ( subject.find(NAUKRI_RATING_5_STAR) != -1):
			rating = '5STAR'

	# Requirement
	requirement = parseSubjectRequirement(subject)

	# Create dir path
	return os.path.join(WORK_DIR, source, requirement, rating)


#----------------------------------------
# Main
#----------------------------------------
setup()

M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
	retCode, data = M.login(EMAIL_ACCOUNT, getpass.getpass())
except imaplib.IMAP4.error:
	logging.error("LOGIN FAILED!!! ")
	sys.exit(1)

logging.debug(retCode, data)

retCode, mailboxes = M.list()
if retCode == RC_OK:
	logging.debug("Mailboxes:")
	logging.debug(mailboxes)

retCode, data = M.select(EMAIL_FOLDER)
if retCode == RC_OK:
	logging.info("Processing mailbox...\n")
	process_mailbox(M)
	M.close()
else:
	logging.error("ERROR: Unable to open mailbox ", retCode)

M.logout()

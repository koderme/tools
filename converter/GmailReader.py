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
import imaplib
import getpass
import email
import email.header
import datetime
import os
import distutils.dir_util
import datetime

# Dir structure
# <source>/<req>/<rating>/<sender>-<yyyymmdd>-<actual-filename>
#
WORK_DIR = 'downloads'

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


def process_mailbox(M):

	"""
	Do something with emails messages in the folder.  
	For the sake of this example, print some headers.
	"""

	retCode, emailArr = M.search(None, EMAIL_CATEGORY)
	if retCode != RC_OK:
		print("No messages found!")
		return

	for msgId in emailArr[0].split():

		retCode, fetchedEmail = M.fetch(msgId, '(RFC822)')
		if retCode != RC_OK:
			print("ERROR getting message", msgId)
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
			#print(dir(part))
			if part.get_content_maintype() == 'multipart':
				#print(part.as_string())
				continue
			if part.get('Content-Disposition') is None:
				#print(part.as_string())
				continue
			origFileName_ = part.get_filename()
			if bool(origFileName_):
				origFileName = origFileName_.lower()
				# Skip images
				if (origFileName.endswith('jpeg') or origFileName.endswith('jpg') or origFileName.endswith('png')):
					continue
				print('message with attachment %s', origFileName)
				fileName = senderName + '-' + NOW_YYYMMDD + '-' + origFileName
				filePath = os.path.join(downloadDir, fileName)
				if not os.path.isfile(filePath) :
					print(fileName)
					fp = open(filePath, 'wb')
					fp.write(part.get_payload(decode=True))
					fp.close()
				else:
					print('error: file(%s) already exist' % (fileName))

		print('----------------------------------------------------');
		print('Message %s: %s' % (msgId, subject))
		print('Raw Date:', msg['Date'])

		# Now convert to local date-time
		date_tuple = email.utils.parsedate_tz(msg['Date'])
		if date_tuple:
			local_date = datetime.datetime.fromtimestamp(
				email.utils.mktime_tz(date_tuple))
			print ("Local Date:", \
				local_date.strftime("%a, %d %b %Y %H:%M:%S"))

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

def currentDate():
	return datetime.datetime.now().strftime ("%Y%m%d")
	
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

def createDir(dirname):
	distutils.dir_util.mkpath(dirname)

#----------------------------------------
# Main
#----------------------------------------

NOW_YYYMMDD = currentDate()

M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
	retCode, data = M.login(EMAIL_ACCOUNT, getpass.getpass())
except imaplib.IMAP4.error:
	print ("LOGIN FAILED!!! ")
	sys.exit(1)

print(retCode, data)

retCode, mailboxes = M.list()
if retCode == RC_OK:
	print("Mailboxes:")
	print(mailboxes)

retCode, data = M.select(EMAIL_FOLDER)
if retCode == RC_OK:
	print("Processing mailbox...\n")
	process_mailbox(M)
	M.close()
else:
	print("ERROR: Unable to open mailbox ", retCode)

M.logout()

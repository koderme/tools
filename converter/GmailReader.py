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


EMAIL_ACCOUNT = "sales.hueklr@gmail.com"

# Use 'INBOX' to read inbox.  Note that whatever folder is specified, 
# after successfully running this script all emails in that folder 
# will be marked as read.
EMAIL_FOLDER = "INBOX"

EMAIL_CATEGORY = 'ALL'
EMAIL_CATEGORY = '(UNSEEN)'

RC_OK = 'OK'

workDir = '.'
downloadDir = 'email_attachment'
if downloadDir not in os.listdir(workDir):
	os.mkdir(downloadDir)


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

		for part in msg.walk():
			if part.get_content_maintype() == 'multipart':
				# print part.as_string()
				continue
			if part.get('Content-Disposition') is None:
				# print part.as_string()
				continue
			fileName = part.get_filename()
			if bool(fileName):
				print('message with attachment %s', fileName)
				filePath = os.path.join(workDir, downloadDir, fileName)
				if not os.path.isfile(filePath) :
					print(fileName)
					fp = open(filePath, 'wb')
					fp.write(part.get_payload(decode=True))
					fp.close()

		# Subject
		hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
		subject = str(hdr)

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



#----------------------------------------
# Main
#----------------------------------------

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

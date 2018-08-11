#!/usr/bin/python3.5

# Make sure you have IMAP enabled in your gmail settings.
# Right now it won't download same file name twice even if their contents are different.

import email
import getpass, imaplib
import os
import sys

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
	os.mkdir('attachments')

try:
	imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
	typ, accountDetails = imapSession.login('sales.hueklr@gmail.com', 'Amacopy29$')
	print('debug')
	if typ != 'OK':
		print('Not able to sign in!')
		raise
	
	imapSession.select('[Gmail]/All Mail')
	print('debug 2')
	typ, data = imapSession.search(None, 'ALL')
	if typ != 'OK':
		print('Error searching Inbox.')
		raise
	
	# Iterating over all emails
	print('debug')
	for msgId in data[0].split():
		print('debug')
		typ, fetchedEmail = imapSession.fetch(msgId, '(RFC822)')
		if typ != 'OK':
			print('Error fetching mail.')
			raise

		emailBody = fetchedEmail[0][1]
		mail = email.message_from_string(emailBody)
		for part in mail.walk():
			print('debug')
			if part.get_content_maintype() == 'multipart':
				# print part.as_string()
				continue
			if part.get('Content-Disposition') is None:
				# print part.as_string()
				continue
			fileName = part.get_filename()

			print('debug')

			if bool(fileName):
				filePath = os.path.join(detach_dir, 'attachments', fileName)
				if not os.path.isfile(filePath) :
					print(fileName)
					fp = open(filePath, 'wb')
					fp.write(part.get_payload(decode=True))
					fp.close()
	imapSession.close()
	imapSession.logout()
except :
	print('Not able to download all attachments.')

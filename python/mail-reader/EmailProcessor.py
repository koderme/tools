#!/usr/bin/python3.6

import sys
sys.path.append('..')

import imaplib
import getpass
import email
import email.header
import os
import logging

from common.Utils import *
from Constants import *
from EmailParseLogic import *
from EmailMessage import *


#-------------------------------------------------
# Email
# This class allows to login, logout, download
# attachements.
#-------------------------------------------------

class EmailProcessor:
	def __init__(self, emailId):
		self.emailId = emailId

	#--------------------------------------------
    # Login
	#--------------------------------------------
	def login(self):
		handler = imaplib.IMAP4_SSL(EMAIL_OTHERS.SERVER)

		try:
			logging.info(self.emailId)
			retCode, data = handler.login(self.emailId, getpass.getpass())
		except imaplib.IMAP4.error:
			logging.error("LOGIN FAILED!!! ")
			sys.exit(1)

		logging.debug('login data: ' + str(data))
		self.handler = handler

	#--------------------------------------------
    # Logout
	#--------------------------------------------
	def logout(self):
		self.handler.close()
		self.handler.logout()
		logging.info('logout')

	#--------------------------------------------
    # Get mail boxes
	#--------------------------------------------
	def getMailBoxes():
		retCode, mailboxes = self.handler.list()
		if retCode == RC_CODE.OK.name:
			logging.debug("Mailboxes:" + mailboxes)

	#--------------------------------------------
    # Process the emails
	#--------------------------------------------
	def process(self, emailBox, emailCategory, destDir):
		logging.debug('process() called')
		retCode, data = self.handler.select(emailBox)
		if retCode == RC_CODE.OK.name:
			logging.info("Fetching emails from : " + emailBox)
			emailMesgs = self.processEmails(emailCategory)
			logging.info('----------------------------------------------------');
			logging.info('Summary')
			logging.info('processed %d messages' % (len(emailMesgs)))
		else:
			logging.error("Unable to open mailbox ", retCode)


	#--------------------------------------------
	# email processor
	#--------------------------------------------
	def processEmails(self, emailCategory):

		logging.debug('processEmails() called')
		# Get all the emails
		retCode, emailArr = self.handler.search(None, emailCategory)
		if retCode !=RC_CODE.OK.name:
			logging.error("No unread emails");
			return

		# Loop for each email message
		emailMesgs = []
		for msgId in emailArr[0].split():

			logging.info('....................................................');
			logging.info('processing email : ' + str(msgId))
			emailMesg = EmailMessage()
			emailMesgs.append(emailMesg)

			retCode, fetchedEmail = self.handler.fetch(msgId, EMAIL_OTHERS.ENCODE)
			if retCode !=RC_CODE.OK.name:
				logging.error("Error fetching message id : ", msgId)
				return

			msg = email.message_from_bytes(fetchedEmail[0][1])

			# Email details
			hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
			emailMesg.messageId = msgId
			emailMesg.receiveDate = convertToLocalDateTime(msg['Date'])
			emailMesg.subject = str(hdr).lower()
			emailMesg.senderName = EmailParseLogic.getSenderName(msg)
			emailMesg.senderEmailId = EmailParseLogic.getSenderEmail(msg)


			# Loop to process part of each email
			for part in msg.walk():

				logging.debug('...processing part of email:' + str(part))
				if part.get_content_maintype() == EMAIL_OTHERS.MULTIPART:
					logging.debug(part.as_string())
					continue

				if part.get(EMAIL_OTHERS.CON_DISP) is None:
					logging.debug(part.as_string())
					continue

				EmailParseLogic.downloadAttachment(part, emailMesg)

			logging.info('...email details : ' + str(emailMesg))

		return emailMesgs

#-------------------------------------------------
#
#-------------------------------------------------
def convertToLocalDateTime(inDate):
	date_tuple = email.utils.parsedate_tz(inDate)
	local_date = ''
	if date_tuple:
		local_date = datetime.datetime.fromtimestamp(
			email.utils.mktime_tz(date_tuple))

	return local_date

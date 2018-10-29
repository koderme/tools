#!/usr/bin/python3.6

from Constants import *

#-------------------------------------------
# Email message
#-------------------------------------------

class EmailMessage:
	def __init__(self):
		self.messageId = '--empty--'
		self.receiveDate = '--empty--'
		self.subject = '--empty--'
		self.body = '--empty--'
		self.senderName = '--empty--'
		self.senderEmailId = '--empty--'
		self.attachments = []

	def __str__(self):
		SEP = '\n\t\t'
		return SEP + \
		'messageId = ' + str(self.messageId) + SEP + \
		'receiveDate = ' + str(self.receiveDate) + SEP + \
		'subject = ' + self.subject + SEP + \
		'body = ' + self.body + SEP + \
		'senderName = ' + self.senderName + SEP + \
		'senderEmailId = ' + self.senderEmailId

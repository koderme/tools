#!/usr/bin/python3.5

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
		SEP = ','
		return '--tbd--'
		return 'messageId:' + self.messageId + SEP + \
		'receiveDate:' + self.receiveDate + SEP + \
		'subject:' + self.subject + SEP + \
		'body:' + self.body + SEP + \
		'senderName:' + self.senderName + SEP + \
		'senderEmailId:' + 'tbd'

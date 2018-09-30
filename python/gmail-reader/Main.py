#!/usr/bin/python3.5


#
import sys
import argparse
sys.path.append('..')

from common.Utils import *
from Constants import *
from EmailProcessor import *
from EmailProcessor import *

# This program is intended to 
#    -- read specified email box
#    -- download the attachment
#    -- parse the CV
#    -- generate report with skill matrix
#

#----------------------------------------
# Parse command line args
#----------------------------------------
def parseArgs(progArgs):
	parser = argparse.ArgumentParser()
	parser.add_argument('-a','--action', help='download|parse', required=True)
	parser.add_argument('-s','--skills', help='skills', required=False)

	return parser.parse_args()

#----------------------------------------
# doAction
#----------------------------------------
def	doAction(cmdArgs):

	if (cmdArgs.action == 'download'):
		doDownload()

	if (cmdArgs.action == 'parse'):
		doParse()

#----------------------------------------
# Specific action
#----------------------------------------
def doDownload():
	logging.info('doing action download')
	mail = EmailProcessor(EMAIL_ID.SALES_HUEKLR_GMAIL)

	mail.login()
	mail.process(
		EMAIL_FOLDER.INBOX.name,
		EMAIL_CATEGORY.UNREAD,
		DOWNLOAD_DIR)
	mail.logout()

#----------------------------------------
# Specific action
#----------------------------------------
def doParse():
	print('extracting meta...');

#----------------------------------------
# Main
#----------------------------------------
logging.basicConfig(level=logging.INFO)
DOWNLOAD_DIR = './downloads'

cmdArgs = parseArgs(sys.argv);

doAction(cmdArgs)

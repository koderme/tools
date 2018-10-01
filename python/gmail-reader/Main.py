#!/usr/bin/python3.5


#
import sys
import argparse
sys.path.append('..')

from common.Utils import *
from Constants import *
from EmailProcessor import *
from DocConverter import *

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
	parser.add_argument('-a','--action', help='download|extract', required=True)
	parser.add_argument('-d','--dir', help='dir', required=True)
	parser.add_argument('-s','--skills', help='skills', required=False)

	return parser.parse_args()

#----------------------------------------
# doAction
#----------------------------------------
def	doAction(cmdArgs):

	if (cmdArgs.action == 'download'):
		doDownload(cmdArgs)

	if (cmdArgs.action == 'parse'):
		doParse(cmdArgs)

#----------------------------------------
# Specific action
#----------------------------------------
def doDownload(cmdArgs):
	logging.info('action:' +cmdArgs.action)
	mail = EmailProcessor(EMAIL_ID.CV_HUEKLR_GMAIL)

	mail.login()
	mail.process(
		EMAIL_FOLDER.INBOX.name,
		EMAIL_CATEGORY.UNREAD,
		cmdArgs.dir)
	mail.logout()

#----------------------------------------
# Specific action
#----------------------------------------
def doParse(cmdArgs):
	logging.info('action:' +cmdArgs.action)
	DocConverter.convertToText(cmdArgs.dir)
	

#----------------------------------------
# Main
#----------------------------------------
logging.basicConfig(level=logging.INFO)

cmdArgs = parseArgs(sys.argv);

doAction(cmdArgs)

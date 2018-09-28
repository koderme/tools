#!/usr/bin/python3.5


#
import sys
import argparse
sys.path.append('..')

from common.Utils import *
from Constants import *
from EmailProcessor import *

# This program is intended to 
#    -- read specified email box
#    -- download the attachment
#    -- parse the CV
#    -- generate report with skill matrix
#

#----------------------------------------
# setup
#----------------------------------------
def parseArgs(progArgs):
	parser = argparse.ArgumentParser()
	parser.add_argument('-a','--action', help='download|x-meta', required=True)
	parser.add_argument('-s','--skills', help='skills', required=False)

	return parser.parse_args()


#----------------------------------------
# setup
#----------------------------------------

def	doAction(cmdArgs):

	if (cmdArgs.action == 'download'):
		doDownload()

	if (cmdArgs.action == 'x-meta'):
		doExtractMeta()

def doDownload():
	logging.info('doing action download')
	mail = EmailProcessor(EMAIL_ID.CV_HUEKLR_GMAIL)

	mail.login()
	mail.process(
		EMAIL_FOLDER.INBOX.name,
		EMAIL_CATEGORY.UNREAD,
		DOWNLOAD_DIR)
	mail.logout()

def doExtractMeta():
	print('extracting meta...');

#----------------------------------------
# Main
#----------------------------------------
logging.basicConfig(level=logging.INFO)
DOWNLOAD_DIR = './downloads'

cmdArgs = parseArgs(sys.argv);

doAction(cmdArgs)

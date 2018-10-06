#!/usr/bin/python3.5


#
import sys
import argparse
sys.path.append('..')

from common.Utils import *
from CvParser import *

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
	parser.add_argument('-a','--action', help='match', required=True)
	parser.add_argument('-s','--skills', help='skills', required=False)
	parser.add_argument('-d','--dir', help='dir', required=True)

	return parser.parse_args()

#----------------------------------------
# doAction
#----------------------------------------
def	doAction(cmdArgs):

	if (cmdArgs.action == 'match'):
		doMatch(cmdArgs)

#----------------------------------------
# Specific action
#----------------------------------------
def doMatch(cmdArgs):
	logging.info('action:' +cmdArgs.action)

	mail = EmailProcessor(EMAIL_ID.CV_HUEKLR_GMAIL)
	CvParser.match(cmdArgs.dir)
	

#----------------------------------------
# Main
#----------------------------------------
logging.basicConfig(level=logging.INFO)

cmdArgs = parseArgs(sys.argv);

doAction(cmdArgs)

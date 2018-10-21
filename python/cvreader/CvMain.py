#!/usr/bin/python3.5


#
import sys
import argparse
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from CvParseImpl import *
from model.CvParseResult import *

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
	parser.add_argument('-a','--action', help='parse', required=True)
	#parser.add_argument('-s','--skills', help='skills', required=False)
	#parser.add_argument('-d','--dir', help='dir', required=True)

	return parser.parse_args()

#----------------------------------------
# doAction
#----------------------------------------
def	doAction(cmdArgs):

	logger.info('cmdArgs:' + str(cmdArgs))
	if (cmdArgs.action == 'parse'):
		doParse(cmdArgs)

#----------------------------------------
# Specific action
#----------------------------------------
def doParse(cmdArgs):
	logger.info('action:' + cmdArgs.action)

	parser = CvParseImpl('temp/test.developer.txt')
	prResult = parser.parse()
	logger.info('parse-result:' + str(prResult))
	

#----------------------------------------
# Main
#----------------------------------------
logger = logging.getLogger('cvreader')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('./debug.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

cmdArgs = parseArgs(sys.argv);

doAction(cmdArgs)

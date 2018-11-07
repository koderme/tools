#!/usr/bin/python3.6


#
import sys
import argparse
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *
from common.MongoDb import *
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
	parser.add_argument('-a','--action', help='parse|parsepersist', required=True)
	#parser.add_argument('-s','--skills', help='skills', required=False)
	#parser.add_argument('-d','--dir', help='dir', required=True)

	return parser.parse_args()

#----------------------------------------
# doAction
#----------------------------------------
def	doAction(cmdArgs):

	try:
		logger.info('cmdArgs:' + str(cmdArgs))
		if (cmdArgs.action == 'parse'):
			doParse(cmdArgs)

		if (cmdArgs.action == 'parsepersist'):
			doParsePersist(cmdArgs)
	except Exception as e:	
		logger.exception(e)


#----------------------------------------
# Specific action
#----------------------------------------
def doParse(cmdArgs):
	prResult = None
	parser = CvParseImpl('../mail-reader/processed/cv5.txt')
	prResult = parser.parse()
	logger.info('--------------------------------')
	logger.info('parse-result:' + str(prResult.getSecDict()))
	logger.info('--------------------------------')
	logger.info('parse-result-json:' + str(prResult.getSecDictAsJson()))
	return prResult

#----------------------------------------
# Specific action
#----------------------------------------
def doParsePersist(cmdArgs):
	connString = 'mongodb://localhost:27017/'
	mdb = MongoDb(connString, "vishal", "vishal", "resim")
	mdb.authenticate()

	pr = doParse(cmdArgs)

	mdb.insertOne("resim", "cv", pr.getSecDict())

#----------------------------------------
# Main
#----------------------------------------
fh1 = logging.StreamHandler()
fh1.setLevel(logging.INFO)

fh2 = logging.FileHandler('./debug.log')
fh2.setLevel(logging.DEBUG)

logger = logging.getLogger('cvreader')
logger.addHandler(fh1)
logger.addHandler(fh2)



cmdArgs = parseArgs(sys.argv);

doAction(cmdArgs)

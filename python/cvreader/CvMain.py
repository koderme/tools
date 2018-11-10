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
	parser.add_argument('-d','--dir', help='dir', required=True)
	#parser.add_argument('-s','--skills', help='skills', required=False)

	return parser.parse_args()

#----------------------------------------
# doAction
#----------------------------------------
def	doAction(cmdArgs):

	try:

		cvExtns = ['txt']
		cvfileList = Utils.getFileList(cmdArgs.dir, cvExtns)

		for filepath in cvfileList:

			logger.info('cmdArgs:' + str(cmdArgs))
			if (cmdArgs.action == 'parse'):
				doParse(filepath)

			if (cmdArgs.action == 'parsepersist'):
				doParsePersist(filepath)
	except Exception as e:	
		logger.exception(e)


#----------------------------------------
# Specific action
#----------------------------------------
def doParse(filepath):
	prResult = None
	parser = CvParseImpl(filepath)
	prResult = parser.parse()
	logger.info('--------------------------------')
	logger.info('parse-result-json:' + str(prResult.getSecDictAsJson()))
	return prResult

#----------------------------------------
# Specific action
#----------------------------------------
def doParsePersist(filepath):
	connString = 'mongodb://localhost:27017/'
	mdb = MongoDb(connString, "vishal", "vishal", "resim")
	mdb.authenticate()

	pr = doParse(filepath)

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

#!/usr/bin/python3.5
#
# Very basic example of using Python 3 and IMAP to iterate over emails in a
# gmail folder/label.  This code is released into the public domain.
#
# This script is example code from this blog post:
# http://www.voidynullness.net/blog/2013/07/25/gmail-email-with-python-via-imap/
#
# This is an updated version of the original -- modified to work with Python 3.4.
#
import sys
sys.path.append('..')

import logging
from common.Utils import *
from EmailMessage import *



#----------------------------------------
# Constants
#----------------------------------------
class MyClass:

	@staticmethod
	def m1():
		logging.info('m1()')

def parseSubject():

	subAttr = {
		'source' : CV_SOURCE.others.name,
		'rating' : 'not-rated',
		'req'    : 'none',
	}

	return subAttr

#----------------------------------------
# setup
#----------------------------------------
def setup():
	logging.basicConfig(level=logging.INFO)


#----------------------------------------
# Main
#----------------------------------------
setup()

logging.info("test %s", "hello world")
MyClass.m1()
em = EmailMessage()
logging.info('em : ' + str(em))
logging.info('source : ' + CV_SOURCE.naukri.name);
logging.info('source : ' + NAUKRI_RATING.S2);
logging.info('source : ' + FILE_EXTN.JPG);



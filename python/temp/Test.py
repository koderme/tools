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

from PIL import Image
import pytesseract
import logging
import argparse
from common.Utils import *



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


def parseArgs(xx):
	parser = argparse.ArgumentParser()
	parser.add_argument('-o','--open-file', help='file to be opended', required=False)
	parser.add_argument('-s','--save-file', help='file to be saved', required=False)

	args = parser.parse_args()

	print("print args----")
	print(args.open_file)
	print(args.save_file)

def itotext():
	filename='image-to-text.JPG'
	text = pytesseract.image_to_string(Image.open(filename))
	print(text)

#----------------------------------------
# Main
#----------------------------------------
setup()
parseArgs(sys.argv)

itotext()




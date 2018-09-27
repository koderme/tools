#!/usr/bin/python3.5
#
#

import sys
import glob
sys.path.append('..')

import os
from pdf2image import convert_from_path
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
	parser.add_argument('-i','--in-dir', help='input dir to be scanned', required=True)

	args = parser.parse_args()

	return args

def imageToText(inFiles):
	text = ''
	outTextFilepath=''
	for f in inFiles:
		outTextFilepath=f + '.txt'
		text += pytesseract.image_to_string(Image.open(f))

	logging.info("writing to " + outTextFilepath)
	f= open(outTextFilepath, "w+")
	f.write(text)
	f.close()

#--------------------------------------------
# Convert pdf to text
#--------------------------------------------
def pdfToText(pdfFilepath):

	# Convert to images
	imageFileList = pdfToImage(pdfFilepath)

	imageToText(imageFileList);

	# Remove imageFileList tbd
	for f in imageFileList:
		logging.info('removing ' + f)
		os.remove(f);

#--------------------------------------------
# Convert pdf to jpg
#--------------------------------------------
def pdfToImage(pdfFilepath):
	pages = convert_from_path(pdfFilepath, 500)
	i=0
	logging.info('converting pdf to image...')
	imageFileList = []
	for page in pages:
		outFilepath=pdfFilepath + str(i) + '.jpg'
		imageFileList.append(outFilepath)
		page.save(outFilepath, 'JPEG')
		i=i+1

	return imageFileList


def convertToText(args):

	for filepath in glob.glob(args.in_dir + '/' + '*.*'):

		logging.info('-----------------------')
		logging.info('processing ' + filepath)
		filepathLower=filepath.lower()

		if (filepathLower.lower().endswith('pdf')):
			pdfToText(filepath)
		elif (filepathLower.endswith("jpeg") or
				filepathLower.endswith('jpg') or
				filepathLower.endswith('png') or
				filepathLower.endswith('gif') ):

			logging.info('converting image to text ...')
			text = pytesseract.image_to_string(Image.open(filepath))
			outFilepath = filepath + '.txt'
			f= open(outFilepath, "w+")
			f.write(text)
			f.close()
		else:
			logging.info('file xtn unknown...skipping...')

#----------------------------------------
# Main
#----------------------------------------
setup()
args = parseArgs(sys.argv)

convertToText(args)



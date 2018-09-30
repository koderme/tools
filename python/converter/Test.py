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
OutputExtension = '.rtf'

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

def imageToText(inFiles, outFilepath):
	text = ''
	for f in inFiles:
		text += pytesseract.image_to_string(Image.open(f))

	logging.info("writing to " + outFilepath)
	f= open(outFilepath, "w+")
	f.write(text)
	f.close()

#--------------------------------------------
# Convert pdf to text
#--------------------------------------------
def pdfToText(pdfFilepath):

	# Convert to images
	outFilepath = Utils.nameWithoutExtn(pdfFilepath) + OutputExtension
	
	imageFileList = pdfToImage(pdfFilepath)

	imageToText(imageFileList, outFilepath);

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


#--------------------------------------------
# Convert image/pdf to text
#--------------------------------------------
def convertToText(args):

	for filepath in glob.glob(args.in_dir + '/' + '*.*'):

		logging.info('-----------------------')
		logging.info('processing : ' + filepath)
		filepathLower=filepath.lower()

		if (filepathLower.lower().endswith('pdf')):
			pdfToText(filepath)
		elif (filepathLower.endswith("jpeg") or
				filepathLower.endswith('jpg') or
				filepathLower.endswith('png') or
				filepathLower.endswith('gif') ):

			logging.info('converting image to text ...')
			text = pytesseract.image_to_string(Image.open(filepath))
			outFilepath = filepath + OutputExtension
			f= open(outFilepath, "w+")
			f.write(text)
			f.close()
		else:
			logging.info('file xtn unknown...skipping...')

#----------------------------------------
# Main
#----------------------------------------
setup()

import os
import tempfile

temp = tempfile.NamedTemporaryFile()
try:
    print('temp.name:' + temp.name)
finally:
    # Automatically cleans up the file
    temp.close()



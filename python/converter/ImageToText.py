#!/usr/bin/python3.6
#
#

import sys
import glob
import tempfile
from pathlib import Path

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

	logging.debug("writing to " + outFilepath)
	f= open(outFilepath, "w+")
	f.write(text)
	f.close()
	logging.info("created text file: " + outFilepath)

#--------------------------------------------
# Convert pdf to text
#--------------------------------------------
def pdfToText(pdfFilepath, outFilepath):

	# Convert to images
	imageFileList = pdfToImage(pdfFilepath)

	imageToText(imageFileList, outFilepath);

	# Remove imageFileList tbd
	for f in imageFileList:
		logging.debug('removing ' + f)
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
		tmpfile = tempfile.NamedTemporaryFile(delete=False)
		imageFileList.append(tmpfile.name)
		page.save(tmpfile.name, 'JPEG')
		i=i+1

	logging.debug('file list: ' + str(imageFileList))
	
	return imageFileList


#--------------------------------------------
# Convert image/pdf to text
#--------------------------------------------
def convertToText(args):

	converted = 0
	skipped = 0
	for filepath in glob.glob(args.in_dir + '/' + '*.*'):

		outFilepath = Utils.nameWithoutExtn(filepath) + OutputExtension

		# Skip file that have been converted
		tmpPath = Path(outFilepath)
		if tmpPath.is_file():
			logging.debug("file already converted...skipping")
			skipped += 1
			continue

		converted += 1
		logging.info('-----------------------')
		logging.info('processing : ' + filepath)

		filepathLower=filepath.lower()

		if (filepathLower.lower().endswith('pdf')):
			pdfToText(filepath, outFilepath)
		elif (filepathLower.endswith("jpeg") or
				filepathLower.endswith('jpg') or
				filepathLower.endswith('png') or
				filepathLower.endswith('gif') ):

			logging.info('converting image to text ...')
			text = pytesseract.image_to_string(Image.open(filepath))
			f= open(outFilepath, "w+")
			f.write(text)
			f.close()
		else:
			logging.debug('file xtn unknown...skipping...')
			i=0

	logging.info('summary : ' +
			'converted = ' + str(converted) + '+' +
			'skipped = ' + str(skipped) )

#----------------------------------------
# Main
#----------------------------------------
setup()
args = parseArgs(sys.argv)

convertToText(args)



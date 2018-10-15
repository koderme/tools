#!/usr/bin/python3.5

import datetime
import time
import os
import distutils.dir_util
import logging
import shutil
from enum import Enum

class Utils:
	def currentDate():
		return datetime.datetime.now().strftime ("%Y%m%d")

	def currentTimestamp():
		return datetime.datetime.now().strftime ("%Y%m%d_%H%M%S")

	def createDir(dirname):
		logging.info('creating dir : ' + dirname)
		distutils.dir_util.mkpath(dirname)

	def move(srcPath, destDir):
		logging.info('moving file : ' + srcPath + ' --> ' + destDir)
		if not os.path.isdir(destDir) :
			Utils.createDir(destDir)
		shutil.move(srcPath, destDir);

	def nameWithoutExtn(filename):
		l=len(filename)-4
		return filename[0:l]

	def sleep(durationInMs):
		time.sleep(durationInMs/1000.0);

	def getText(inFilepath):
		str1 = open(inFilepath, 'r').read()
		return str1

	def getTextLines(inFilepath):
		f = open(inFilepath, 'r+')
		lineList = []
		for line in f.readlines():
			lineList.append(line)
		f.close()

		return lineList

#----------------------------------------
# MyEnum
#----------------------------------------
def MyEnum(**enums):
	return type('Enum', (), enums)

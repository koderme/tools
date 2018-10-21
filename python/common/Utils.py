#!/usr/bin/python3.5

import datetime
import time
import re
import os
import distutils.dir_util
import logging
import shutil
import unittest

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


	# It tokenizes the specified line using nltp.
	# @param line
	# @return list of words with length > 1
	#
	def wordTokenizeNltk(line):
		wordList = word_tokenize(line)
		return list(filter(lambda x: len(x) > 1, wordList))

	def stripWordsInList(wordList):
		return list(map(lambda x:x.strip(), wordList))

	#--------------------------------------------------
	# Split the line using delimiters which are non-words
	# @param Line to be split
	# @return List contains words
	#--------------------------------------------------
	def getWords(inStr):
		re1 = r'\w+'
		list1=re.findall(re1, inStr)
		return list1 

	def removeDups(inList):
		return list(set(inList))

	# re.match matches begining of str
	def match(regex, str1):
		resultObj = re.match(regex, str1, re.I)
		if (resultObj):
			return True
		else:
			return False

	# re.search matches anywhere in string
	def search(regex, str1):
		resultObj = re.search(regex, str1, re.I)
		if (resultObj):
			return True
		else:
			return False

#----------------------------------------
# MyEnum
#----------------------------------------
def MyEnum(**enums):
	return type('Enum', (), enums)

#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestThisClass(unittest.TestCase):

	def test_getWords(self):

		# ----------------------
		toks = Utils.getWords('hello how are you')
		self.assertEqual(4, len(toks))
		# ----------------------
		toks = Utils.getWords('hello how|are you')
		self.assertEqual(4, len(toks))
		# ----------------------
		toks = Utils.getWords('hello how|are,you')
		self.assertEqual(4, len(toks))
		# ----------------------
		toks = Utils.getWords('hello |||| * . (how)     are\nyou')
		self.assertEqual(4, len(toks))

		# ----------------------
		toks = Utils.getWords('')
		self.assertEqual(0, len(toks))
		# ----------------------
		toks = Utils.getWords(' 	\n')
		self.assertEqual(0, len(toks))

	def test_stripWordsInList(self):
		wordList = [ ' test0', ' test1 ' , '    	test2		' ]
		strippedList = Utils.stripWordsInList(wordList)

		self.assertEqual('test0', strippedList[0])
		self.assertEqual('test1', strippedList[1])
		self.assertEqual('test2', strippedList[2])


	def test_search(self):
		re1 = 'first\s+second'
		result = Utils.search(re1, 'first second')
		self.assertEqual(result, True)
		
		result = Utils.search(re1, 'first  second')
		self.assertEqual(result, True)
		
		result = Utils.search(re1, 'first          second')
		self.assertEqual(result, True)
		
		result = Utils.search(re1, 'fIrst          secoNd')
		self.assertEqual(result, True)



# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestThisClass)
unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/python3.5

import os
import re
import unittest
import sys
sys.path.append('..')

from nltk.tokenize import sent_tokenize, word_tokenize


# Common functions 

class Common:
	# It tokenizes the specified line using nltp.
	# @param line
	# @return list of words with length > 1
	#
	def wordTokenize(line):
		wordList = word_tokenize(line)
		return list(filter(lambda x: len(x) > 1, wordList))



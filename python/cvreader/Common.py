#!/usr/bin/python3.5

import os
import re
import unittest

from nltk.tokenize import sent_tokenize, word_tokenize


# Common functions 

class Common:

#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestThisClass(unittest.TestCase):

	def test_mysplit(self):

		# ----------------------
		line = 'hello how are you'
		delims = [ ' ' ]
		toks = Common.mysplit(line)
		self.assertEqual(4, len(toks))
		# ----------------------
		line = 'hello how|are you'
		delims = [ ' ', '|', ]
		toks = Common.mysplit(line)
		self.assertEqual(4, len(toks))
		# ----------------------
		line = 'hello how|are,you'
		delims = [ ' ', '|', ',' ]
		toks = Common.mysplit(line)
		self.assertEqual(4, len(toks))
		# ----------------------
		line = 'hello   how     are\nyou'
		delims = [ '\s+']
		toks = Common.mysplit(line)
		self.assertEqual(4, len(toks))



# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestThisClass)
unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/python3.6

import os
import unittest
import sys

class MyClass:

	# re.match matches begining of str
	def match(regex, str1):
		resultObj = re.match(regex, str1, re.I)
		if (resultObj):
			return True
		else:
			return False


#------------------------------------------
# Unit test
#------------------------------------------
class TestMyClass(unittest.TestCase):

	def test_search(self):
		re1 = 'first\s+second'
		result = MyClass.search(re1, 'first second')
		self.assertEqual(result, True)

		result = MyClass.search(re1, 'first  second')
		self.assertEqual(result, True)

		result = MyClass.search(re1, 'first 		 second')
		self.assertEqual(result, True)

		result = MyClass.search(re1, 'fIrst 		 secoNd')
		self.assertEqual(result, True)

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
unittest.TextTestRunner(verbosity=2).run(suite)

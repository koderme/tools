#!/usr/bin/python3.5

import os
import re
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

	# re.search matches anywhere in string
	def search(regex, str1):
		resultObj = re.search(regex, str1, re.I)
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

	def test_search1(self):
		re1 = '(one|two)\s+three'
		result = MyClass.search(re1, 'xxYYss two')
		self.assertEqual(result, False)
		result = MyClass.search(re1, 'one three')
		self.assertEqual(result, True)
		result = MyClass.search(re1, 'two  three')
		self.assertEqual(result, True)

	def test_search2(self):
		re1 = '((11|12)\s+13|(21|22)\s+23)'
		result = MyClass.search(re1, 'xxYYss 13')
		self.assertEqual(result, False)
		result = MyClass.search(re1, '11 13')
		self.assertEqual(result, True)
		result = MyClass.search(re1, '12  13')
		self.assertEqual(result, True)

		result = MyClass.search(re1, '21  23')
		self.assertEqual(result, True)
		result = MyClass.search(re1, '22  23')
		self.assertEqual(result, True)

	def test_search3(self):
		re1 = r'\btest.*\b'
		self.assertEqual(True, MyClass.search(re1, 'test'))
		self.assertEqual(True, MyClass.search(re1, 'tested'))
		self.assertEqual(True, MyClass.search(re1, 'testing'))
		self.assertEqual(False, MyClass.search(re1,'intestxxx'))
		self.assertEqual(False, MyClass.search(re1,'tesx'))

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
unittest.TextTestRunner(verbosity=2).run(suite)

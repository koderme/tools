#!/usr/bin/python3.6

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

		print('result:' + str(resultObj))
		if (resultObj):
			return True
		else:
			return False

	# re.search matches anywhere in string
	def searchWithGroup(regex, str1):
		resultObj = re.search(regex, str1, re.I)
		if (resultObj):
			return float(resultObj.group(1))
		else:
			return -1

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

	def test_search4(self):
		re1 = r'(\d{1,2}.\d{0,2}|\d{1,2}\.\d{1,2}).*(years|yr).*(experience)'
		x = MyClass.searchWithGroup(re1, 'i have 12 years of experience in')
		self.assertEquals(12, x)
		x = MyClass.searchWithGroup(re1, 'i have 12. years of experience in')
		self.assertEquals(12, x)
		x = MyClass.searchWithGroup(re1, 'i have 12.3 years of experience in')
		self.assertEquals(12.3, x)
		x = MyClass.searchWithGroup(re1, 'i have 12.34 years of experience in')
		self.assertEquals(12.34, x)
		x = MyClass.searchWithGroup(re1, 'i have 11.345 years of experience in')
		self.assertEquals(11.34, x)
		x = MyClass.searchWithGroup(re1, 'i have  0.34 years of experience in')
		self.assertEquals(0.34, x)
		x = MyClass.searchWithGroup(re1, 'i have  0.22. years of experience in')
		self.assertEquals(0.22, x)
		x = MyClass.searchWithGroup(re1, 'i have  0.33. yr of experience in')
		self.assertEquals(0.33, x)
		x = MyClass.searchWithGroup(re1, 'i have 44.55years of experience in')
		self.assertEquals(44.55, x)
		x = MyClass.searchWithGroup(re1, 'i have 55.66 years sd e  experience in')
		self.assertEquals(55.66, x)

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
unittest.TextTestRunner(verbosity=2).run(suite)

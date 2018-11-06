#!/usr/bin/python3.6

import os
import unittest
import sys
sys.path.append('..')

l_noop = lambda a1, a2: 0
l_add = lambda a1, a2: a1 + a2
l_sub = lambda a1, a2: a1 - a2
l_complex_lambda = lambda a1, a2:(f1(), f2(), f3())[-1]
l_arr = lambda arr1:print(str(arr1))

def f1():
	10 + 10

def f2():
	20 + 20

def f3():
	return 300

class MyClass:
	def __init__(self, name, lambdaFunc=l_noop):
		self.name = name
		self.result = 0
		if (lambdaFunc == None):
			self.lambdaFunc = l_noop
		else:
			self.lambdaFunc = lambdaFunc

	def invoke(self, a, b):
		self.result = self.lambdaFunc(a,b)

	def invokeArr(self, arr):
		self.lambdaFunc(arr)

	def getResult(self):
		return self.result

#------------------------------------------
# Unit test
#------------------------------------------
class TestMyClass(unittest.TestCase):

	def test_lambda_default(self):
		obj = MyClass('test')
		obj.invoke(20, 5)	
		self.assertEqual(0, obj.getResult())

	def test_lambda_with_arg(self):
		obj = MyClass('test', l_add)
		obj.invoke(20, 5)	
		self.assertEqual(25, obj.getResult())

	def test_lambda_with_complex_lambda(self):
		obj = MyClass('test', l_complex_lambda)
		obj.invoke(20, 5)	
		self.assertEqual(300, obj.getResult())

	def test_lambda_with_arr(self):
		obj = MyClass('test', l_arr)
		obj.invokeArr([4, 5, 10, 1])


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
unittest.TextTestRunner(verbosity=2).run(suite)

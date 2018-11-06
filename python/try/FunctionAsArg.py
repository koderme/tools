#!/usr/bin/python3.6

import os
import unittest
import sys


def add(a, b):
		return a+b

def subtract(a, b):
		return a-b

def noop(a, b):
		pass

def addArr(arr):
	sum = 0
	for x in arr:
		sum +=x
	return sum

class MyClass:
	def __init__(self, func):
		self.result = 0
		self.func = func

	def invoke(self, a, b):
		self.result = self.func(a,b)

	def invokeArr(self, arr):
		self.result = self.func(arr)

	def getResult(self):
		return self.result

#------------------------------------------
# Unit test
#------------------------------------------
class TestMyClass(unittest.TestCase):

	def test_func_add(self):
		obj = MyClass(add)
		obj.invoke(20, 5)	
		self.assertEqual(25, obj.getResult())

	def test_func_subtract(self):
		obj = MyClass(subtract)
		obj.invoke(20, 5)	
		self.assertEqual(15, obj.getResult())

	def test_func_arg_w_arr(self):
		arr1 = [ 1, 2, 3, 4, 5]
		obj = MyClass(addArr)
		obj.invokeArr(arr1)
		self.assertEqual(15, obj.getResult())


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
unittest.TextTestRunner(verbosity=2).run(suite)

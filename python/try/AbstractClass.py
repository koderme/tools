#!/usr/bin/python3.6

import abc
import os
import unittest
import sys
sys.path.append('..')


class MyAbstract(object, metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def __str__(self):
		pass

	@abc.abstractmethod
	def f1(self):
		pass

	def baseMethod(self):
		print('MyAbstract:baseMethod')



class MyAbstractImpl(MyAbstract):
	def __str__(self):
		return 'MyAbstractImpl!'

	def f1(self):
		print('MyAbstractImpl:f1')
		self.baseMethod()



obj = MyAbstractImpl()
print('obj:' + str(obj))

obj.f1()

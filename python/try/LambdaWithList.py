#!/usr/bin/python3.6

import os
import unittest
import sys
sys.path.append('..')

l_noop = lambda a1, a2: 0
l_add = lambda a1, a2: a1 + a2
l_sub = lambda a1, a2: a1 - a2
l_printer = lambda x:print(x)



#------------------------------------------
# Unit test
#------------------------------------------
class TestMyClass(unittest.TestCase):

	def test_1(self):
		arr1 = [1, 2, 3 ]
		y = list(map(l_printer, arr1))
		print('result:' + str(y))


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/python3.6

import os
import re
import unittest
import sys

class MyClass:

	def dict_initialize():
		people = {
			1: {'name': 'John', 'age': '27', 'sex': 'Male'},
			2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
			'?': 'something else'
			}

		print('len of dict : ' + str(len(people)))

		for p_id, p_info in people.items():
			print("\npid:" + str(p_id) + " ===> " + str(p_info)) 

	def dict_add_elements_separately():
		people = { }

		# Initialize to empty
		people[2] = {}

		people[2]['name'] = 'n1'
		people[2]['age'] = '10'
		people[2]['sex'] = 'male'
		print('len of dict : ' + str(len(people)))

		for p_id, p_info in people.items():
			print("\npid:" + str(p_id) + " ===> " + str(p_info)) 
 
#------------------------------------------
# Unit test
#------------------------------------------
class TestMyClass(unittest.TestCase):

	def test_1(self):
		MyClass.dict_initialize()
		MyClass.dict_add_elements_separately()


# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
unittest.TextTestRunner(verbosity=2).run(suite)

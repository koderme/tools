#!/usr/bin/python3.5

import os
import abc

import sys
sys.path.append('..')

from CvParseResult import *

#----------------------------------------------------
# CvParse is abstract class.
# It exposes API for parsing CV.
#
#----------------------------------------------------
class CvParse:
	def __init__(self, inFilepath):
		self.inFilepath = inFilepath

	#------------------------------------------------
	# Parses the <inFilePath>
	# @return CvParseResult
	#------------------------------------------------
	@abc.abstractmethod
	def parse(self):
		pass

#!/usr/bin/python3.6

import os
import abc

import sys
sys.path.append('..')

from model.CvParseResult import *

#----------------------------------------------------
# CvParse is abstract class.
# It exposes API for parsing CV.
#
#----------------------------------------------------
class CvParse(object, metaclass=abc.ABCMeta):
	def __init__(self, inFilepath):
		self.inFilepath = inFilepath

	#------------------------------------------------
	# Parses the <inFilePath>
	# @return CvParseResult
	#------------------------------------------------
	@abc.abstractmethod
	def parse(self):
		pass

#!/usr/bin/python3.5

import datetime
import distutils.dir_util
import logging
from enum import Enum

class Utils:
	def currentDate():
		return datetime.datetime.now().strftime ("%Y%m%d")

	def currentTimestamp():
		return datetime.datetime.now().strftime ("%Y%m%d_%H%M%S")

	def createDir(dirname):
		distutils.dir_util.mkpath(dirname)

	def nameWithoutExtn(filename):
		l=len(filename)-4
		return filename[0:l]

#----------------------------------------
# MyEnum
#----------------------------------------
def MyEnum(**enums):
	return type('Enum', (), enums)

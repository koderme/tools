#!/usr/bin/python3.5

import datetime
import distutils.dir_util

def currentDate():
	return datetime.datetime.now().strftime ("%Y%m%d")

def currentTimestamp():
	return datetime.datetime.now().strftime ("%Y%m%d_%H%M%S")

def createDir(dirname):
	distutils.dir_util.mkpath(dirname)


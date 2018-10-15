#!/usr/bin/python3.5
import sys
sys.path.append('..')
sys.path.append('../..')

from Common import *
from common.Utils import *


class Ref:
	Tag =  Enum('', 'summary skill role project employer certification personal')
	Section =  Enum('', 'unknown default personal summary skill workhistory project education certification address objective')
	LineType =  Enum('', 'SectionHeader SectionBody Others')
	DefaultLocation =  'others'
	LocationDict = {
				'bengaluru' : 'bangalore',
				'bangalore' : 'bangalore',
				'banglore'  : 'bangalore',

				'mumbai' : 'mumbai',
				'bombay' : 'mumbai',
				'vashi' : 'mumbai',

				'hyderabad' : 'hyderabad',
				'hydrabad' : 'hyderabad',

				'chennai' : 'chennai',
				'chennai' : 'chennai',

				'delhi' : 'delhi',
				'new delhi' : 'delhi',
				'ncr' : 'delhi',

				'gurgaon' : 'gurgaon',
				'gurugram' : 'gurgaon',

				'noida' : 'noida',

				'indore' : 'indore',
				'mangalore' : 'mangalore',
				'pune' : 'pune',
				'nagpur' : 'nagpur',

				'ahmedabad' : 'ahmedabad',
		}

	def getLocation(line):
		wordList = Common.wordTokenize(line)
		location = ''
		for word in wordList:
			location = Ref.LocationDict.get(word, Ref.DefaultLocation)
			if (location != Ref.DefaultLocation):
				return location

		return location



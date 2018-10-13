#!/usr/bin/python3.5
import sys
sys.path.append('..')

from common.Utils import *
from Common import *




class Ref:
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
			print('finding [' +word + '] in dict')
			location = Ref.LocationDict.get(word, Ref.DefaultLocation)
			if (location != Ref.DefaultLocation):
				return location

		return location



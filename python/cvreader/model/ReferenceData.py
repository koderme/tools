#!/usr/bin/python3.6

import os
import unittest
import sys
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *

class Ref:
	Tag =  Enum('', 'summary skill role project employer certification personal')
	Section =  Enum('', 'unknown default personal summary skill workhistory project education certification address objective')

	PossibleSectionHeader = [
			'personal', 'aboutme', 'professional', 'profile',
			'experience', 'summary', 'skill', 'work',
			'career', 'history', 'assignment', 'scholastic',
			'education', 'qualification', 'cerfitication', 'certified',
			'project', 'objective', 'address', 'residence', 'skills'
		]

	PossibleProjectHeader = [
		'project', 'title', 'description',
		'client','organization',
		'duration',
		'role', 'responsibilities', 'position',
		'contribution', 'deliverables',
		'team size','team',
		'environment',
		'techology', 'technologies', 'techstack', 'tech', 'platform','tools',
		]

	PossibleWorkHistoryHeader = [
		'designation', 'role',
		'organization', 'employer',
		'duration', 'period',
		'location', 'place',
		]

	Verbs = [
		'used',
		]

	LineType =  Enum('', 'SectionHeader SectionBody Others')
	DefaultLocation =  'location-not-found'
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

	DefaultEducation =  'edu-not-found'
	EducationDict = { 
			'be'   : 'be',
			'btech' : 'btech',

			'bachelor' : 'bachelor',
			'master' : 'master',

			'technology' : 'technology',
			'engineering' : 'engineering',
			'science' : 'science',
			'commerce' : 'commerce',
			'arts' : 'art',
			'finance' : 'finance',
			'marketing' : 'marketing',

			'bsc' : 'bsc',
			'bcom' : 'bCom',
			'ba' : 'ba',
			'bba' : 'bba',
			'cfa' : 'cfa',

			'msc' : 'msc',
			'mca' : 'mca',
			'mba' : 'mba'
	}

	#--------------------------------------------------
	# Finds matching word from line in the specified
	# searchDict.
	# @param Line containing words to be searched.
	# @param searchDict Dict to be searched
	# @param defaultWhenNotFound 
	# @return list containing lookup result.
	#--------------------------------------------------
	def lookupFromDict(line, searchDict, defaultWhenNotFound, findAll=False):
		wordList = Utils.getWords(line)

		lookupResultArr = []
		for word in wordList:
			result = searchDict.get(word, defaultWhenNotFound)
			if (result != defaultWhenNotFound):
				lookupResultArr.append(result)
				if (not findAll):
					break

		if (len(lookupResultArr) == 0):
			lookupResultArr.append(defaultWhenNotFound)

		# Remove dups
		return Utils.removeDups(lookupResultArr)

	#--------------------------------------------------
	# Lookup matching location
	# @param Line containing keywords to be lookedup
	# @return list contains lookedup values
	#--------------------------------------------------
	def findLocation(line):
		return Ref.lookupFromDict(line, Ref.LocationDict, Ref.DefaultLocation, True)

	#--------------------------------------------------
	# Lookup matching education
	# @param Line containing keywords to be lookedup
	# @return list contains lookedup values
	#--------------------------------------------------
	def findEducation(line):
		return Ref.lookupFromDict(line, Ref.EducationDict, Ref.DefaultEducation, True)

#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestThisClass(unittest.TestCase):

	def test_lookupFromDict(self):

		# ----------------------
		line = 'places visited bengaluru chennai mumbai'
		toks = Ref.lookupFromDict(line, Ref.LocationDict, Ref.DefaultLocation, True)
		self.assertEqual(3, len(toks))

		# ----------------------
		line = 'places visited bengaluru bangalore bombay mumbai'
		toks = Ref.lookupFromDict(line, Ref.LocationDict, Ref.DefaultLocation, True)
		self.assertEqual(2, len(toks))

		# ----------------------
		line = 'places visited bangalore-32'
		toks = Ref.lookupFromDict(line, Ref.LocationDict, Ref.DefaultLocation, True)
		self.assertEqual(1, len(toks))
		self.assertEqual('bangalore', toks[0])

		# ----------------------
		line = 'places visited somecity'
		toks = Ref.lookupFromDict(line, Ref.LocationDict, Ref.DefaultLocation, True)
		self.assertEqual(1, len(toks))
		self.assertEqual(Ref.DefaultLocation, toks[0])

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestThisClass)
unittest.TextTestRunner(verbosity=2).run(suite)

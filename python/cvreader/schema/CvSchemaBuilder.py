#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *

from schema.CvSection import *
from model.ReferenceData import *
from rules.CvSectionParseRules import *

logger = logging.getLogger('cvreader')
#-------------------------------------------------------------
# CvSchemaBuilder is responsible for building the CvSchema.
#-------------------------------------------------------------
class CvSchemaBuilder:

	#--------------------------------------------------------
	# It builds the schema metadata.
	#--------------------------------------------------------
	def buildSectionsForSchema():
		sections = []


		sec = CvSection(Ref.Section.personal.name,
					'(personal|aboutme)',
					parsePersonal)
		sections.append(sec)

		sec = CvSection(Ref.Section.summary.name,
					'(professional\s+summary|profile\s+summary)')
		sections.append(sec)

		sec = CvSection(Ref.Section.skill.name,
					'(skill|skills|skillset)',
					parseSkill)
		sections.append(sec)

		sec = CvSection(Ref.Section.workhistory.name,
					'((work|career)\s+history|experience)')
		sections.append(sec)

		sec = CvSection(Ref.Section.project.name,
					'(project\s+summary|assignment\s+history|project)')
		sections.append(sec)

		sec = CvSection(Ref.Section.education.name,
					'(qualification|education|scholastic)',
					parseEducation)
		sections.append(sec)

		sec = CvSection(Ref.Section.certification.name,
					'(certification|certified)')
		sections.append(sec)

		sec = CvSection(Ref.Section.address.name,
					'(address|residence)')
		sections.append(sec)

		sec = CvSection(Ref.Section.objective.name,
					'(objective)')
		sections.append(sec)

		# Default must be last section
		sec = CvSchemaBuilder.getDefaultSection()
		sections.append(sec)

		return sections

	def getDefaultSection():
		return CvSection(Ref.Section.default.name, '.*', parseDefault)

#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestCvSchemaBuilder(unittest.TestCase):

	def test_none(self):
		pass

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSchemaBuilder)
unittest.TextTestRunner(verbosity=2).run(suite)

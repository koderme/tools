#!/usr/bin/python3.5

import os
import unittest
import sys
sys.path.append('..')
sys.path.append('../..')

from common.Utils import *

from schema.CvSection import *
from model.ReferenceData import *
from rules.CvSectionParseRules import *

#-------------------------------------------------------------
# CvSchemaBuilder is responsible for building the CvSchema.
#-------------------------------------------------------------
class CvSchemaBuilder:

	#--------------------------------------------------------
	# It builds the schema metadata.
	#--------------------------------------------------------
	def buildSectionsForSchema():
		sections = []
		sec = CvSection(Ref.Section.unknown.name, [])
		sections.append(sec)
		sec = CvSection(Ref.Section.default.name, [], parseDefault)
		sections.append(sec)
		sec = CvSection(Ref.Section.personal.name, ['personal', 'aboutme'], parsePersonal)
		sections.append(sec)
		sec = CvSection(Ref.Section.summary.name, ['professional summary', 'profile summary'])
		sections.append(sec)
		sec = CvSection(Ref.Section.skill.name, ['skill'], parseSkill)
		sections.append(sec)
		sec = CvSection(Ref.Section.workhistory.name, ['work history', 'career history', 'experience'])
		sections.append(sec)
		sec = CvSection(Ref.Section.project.name, ['project summary', 'assignment history'])
		sections.append(sec)
		sec = CvSection(Ref.Section.education.name, ['qualification', 'education', 'scholastic'])
		sections.append(sec)
		sec = CvSection(Ref.Section.certification.name, ['certification'])
		sections.append(sec)
		sec = CvSection(Ref.Section.address.name, ['address', 'residence'])
		sections.append(sec)
		sec = CvSection(Ref.Section.objective.name, ['objective'])
		sections.append(sec)

		return sections

#---------------------------------------------------------------
# Unit tests
#---------------------------------------------------------------
class TestCvSchemaBuilder(unittest.TestCase):

	def test_none(self):
		pass

# Run unit tests
#if __name__ == '__main__':
#unittest.main()
logging.basicConfig(level=logging.INFO)
suite = unittest.TestLoader().loadTestsFromTestCase(TestCvSchemaBuilder)
unittest.TextTestRunner(verbosity=2).run(suite)

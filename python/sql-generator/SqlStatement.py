#!/usr/bin/python

KEY_SELECT = 'select '
KEY_INSERT = 'insert into '
KEY_FROM = ' from'
KEY_VALUES = ' values'
KEY_DUAL = ' dual'
KEY_UNION = ' union'
KEY_ORB = ' ('
KEY_CRB = ' )'
KEY_SC = ' ;'

class SqlStatement:

	def __init__(self, table):
		self.table = table

	def generateSelect(self, rowCount):
		rowString = ''
		for i in range(rowCount):
			colString = KEY_SELECT

			colString = colString + self.table.toString(i)

			colString = colString + ' ' + KEY_FROM + KEY_DUAL
			if (i < rowCount-1):
				colString = colString + KEY_UNION
			rowString = rowString  + '\n\r' + colString

		return rowString + KEY_SC

	def generateInsert(self):
		colString = KEY_INSERT
		colString = colString +  self.table.schemaTableName()
		colString = colString +  KEY_ORB
		colString = colString +  self.table.columnName(",")
		colString = colString +  KEY_CRB
		return colString

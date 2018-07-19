#!/usr/bin/python

class Table:

	def __init__(self, schemaName, tableName):
		self.schemaName = schemaName
		self.tableName = tableName
		self.colArr=[]

	def toString(self):
		return self.schemaName  + '.' + self.tableName + self.colArr

	def add(self, col):
		self.colArr.append(col)

	def schemaTableName(self):
		return self.schemaName + '.' + self.tableName

	def columnName(self, separator):
		retStr = ''
		i = len(self.colArr)
		for col in self.colArr:
			i = i-1
			retStr = retStr + col.name()
			if (i > 0):
				retStr = retStr + separator
		return retStr


	def toString(self, rowIndex):
		colString = ''
		i = len(self.colArr)
		for col in self.colArr:
			i = i-1
			colString = colString + col.toStringWithValue(rowIndex)
			if (i > 0):
				colString = colString + ','

		return colString



#!/usr/bin/python

class Column:
	DT_NUM = 'number'
	DT_STR = 'string'
	DT_DATE = 'date'
	DT_AUTO = 'auto'
	quote = '\''

	FMT_2d = '{:0>2d}'
	FMT_3d = '{:0>3d}'
	FMT_4d = '{:0>4d}'
	FMT_5d = '{:0>5d}'
	FMT_6d = '{:0>6d}'
	FMT_7d = '{:0>7d}'
	FMT_8d = '{:0>8d}'
	FMT_9d = '{:0>9d}'
	FMT_10d = '{:0>10d}'
	FMT_16d = '{:0>16d}'
	FMT_EMPTY = '{}'
	tbd = '{}'

	def __init__(self, colName, colType, colValuePrefix, colValue, colFormat):
		self.colName = colName
		self.colType = colType
		self.colValuePrefix = colValuePrefix
		self.colValue = colValue
		self.colFormat = colFormat

	def name(self):
		return self.colName

	def toString(self):
		return self.colName  + self.colType  + self.colValuePrefix  + self.colFormat 

	def toStringWithValue(self, rowIndex):

		if (self.colType == self.DT_NUM or self.colType == self.DT_AUTO):
			self.quote = ''

		useFormat = self.colFormat
		if (len(self.colValue) > 0):
			if (self.colFormat != self.FMT_EMPTY):
				useFormat = self.FMT_EMPTY
				print(" warn: col {} --- format changed from {} --> {}".format(self.colName, self.colFormat, useFormat))
			return ' ' + self.quote + self.colValuePrefix + useFormat.format(self.colValue)  + self.quote
		else:
			return ' ' + self.quote + self.colValuePrefix + useFormat.format(rowIndex)  + self.quote

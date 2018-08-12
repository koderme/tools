#!/usr/bin/python3.5

import docx
import os

from docx import Document

def getText(filename):
	print("---------------------------")
	print(filename)
	doc = docx.Document(filename)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.text)
	return '\n'.join(fullText)


def getFile(dirName):
	x = [f.name for f in os.scandir() if f.is_file()]
	print(x)


fname = '../temp/jagadeesh-karri.docx';
x = getText(fname);
print(x)
#getFile('.');


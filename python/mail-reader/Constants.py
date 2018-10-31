#!/usr/bin/python3.6
#

from named_constants import Constants
from enum import Enum

import sys
sys.path.append('..')

from common.Utils import *

#----------------------------------------
# Email related
#----------------------------------------
EMAIL_FOLDER = Enum('', 'INBOX TBD')

EMAIL_OTHERS = MyEnum(
	MULTIPART = 'multipart',
	ENCODE    = '(RFC822)',
	SUBJECT   = 'subject',
	SERVER    = 'imap.gmail.com',
	CON_DISP  = 'Content-Disposition',
	)

EMAIL_CATEGORY = MyEnum(
	ALL = 'ALL',
	UNREAD = '(UNSEEN)'
	)

EMAIL_ID =  MyEnum(
	SALES_HUEKLR       = 'sales@hueklr.com',
	SALES_HUEKLR_GMAIL = 'sales.hueklr@gmail.com',
	CV_HUEKLR_GMAIL    = 'cv.hueklr@gmail.com',
)

#----------------------------------------
# File types
#----------------------------------------
FILE_EXTN = MyEnum(
	JPG  = 'jpg',
	JPEG = 'jpeg',
	PNG  = 'png',
	DOCX = 'docx',
	DOC  = 'doc',
	PDF  = 'pdf',
	)

#----------------------------------------
# CV
#----------------------------------------
CV_SOURCE = Enum('', 'naukri hirist others')

NAUKRI_RATING = MyEnum(
	S2='2 star applicant',
	S3='3 star applicant',
	S4='4 star applicant',
	S5='5 star applicant',
	)

#----------------------------------------
# Dir 
#----------------------------------------
DIRS = MyEnum(
	DOWNLOAD_DIR = './downloads',
	LOG_DIR = '/var/tmp/gmail/'
	)

#----------------------------------------
# Others
#----------------------------------------
RC_CODE = Enum('', 'OK ERROR')



#!/usr/bin/python3.5


#
import sys
sys.path.append('..')

from common.Utils import *
from Constants import *
from EmailProcessor import *

# This program is intended to 
#    -- read specified email box
#    -- download the attachment
#    -- parse the CV
#    -- generate report with skill matrix
#

#----------------------------------------
# setup
#----------------------------------------


#----------------------------------------
# Main
#----------------------------------------
logging.basicConfig(level=logging.INFO)
DOWNLOAD_DIR = './downloads'

mail = EmailProcessor(EMAIL_ID.CV_HUEKLR_GMAIL)

mail.login()
mail.process(
		EMAIL_FOLDER.INBOX.name,
		EMAIL_CATEGORY.UNREAD,
		DOWNLOAD_DIR)
mail.logout()


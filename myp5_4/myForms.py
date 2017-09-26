##############################################################################
#Name : BINOD KATWAL                      					Date: 04/25/17
#Class : CS316 
#Project:  05 
##############################################################################

from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired
import simplejson as json

# Aform  will get Races.json fille
class AForm(Form):
	#declare
	fileToSearch={}
	maxOrmin ={}	
	statToSearch={}
	whatToMatch = {}
	matchValue ={}
	Err = False



        filetoOpen = 'myp5_4/static/Races.json' # open the file .json
  
	def __init__(self):
		try:
  			self.f = open(AForm.filetoOpen, 'r') # read the file if valid or not
    		except IOError:
			print "Error: can\'t find Races.json"
			Err = True
			# if found, perform below f
		else:
			self.contents = self.f.read()
			self.f.close();
    			self.statInfo = json.loads(self.contents)
		   
   	
			AForm.statToSearch= self.statInfo['stats'] #stat
			AForm.fileToSearch= self.statInfo['races'] #Race Names
			AForm.WhatToMatch = self.statInfo['match'] #what tomatch 
			


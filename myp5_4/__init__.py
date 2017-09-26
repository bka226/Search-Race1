##############################################################################
#Name : BINOD KATWAL                      					Date: 04/25/17
#Class : CS316 
#Project:  05 
##############################################################################

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from myp5_4 import views

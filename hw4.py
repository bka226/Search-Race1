#!/usr/bin/python
##############################################################################
#Name : BINOD KATWAL                      		Date: 04/25/17
#Class : CS316 
#Project:  05 
##############################################################################
# The code below generate random port number between min and max value by  deleting (portNum = 2555 ) 
# or comment appropriate port number (portNum = 2555 )
#

from myp5_4 import app
import random
if __name__ == '__main__':


	#range is between 1300 to 9433
	#you can change the range by changing
 	#MAXPORT and MINPORT inside the script

	MAXPORT = 11111 # max
	MINPORT = 1333 #min
	
	portNum = random.randrange(MINPORT, MAXPORT, 1) # Generate the random port number
	

	# if we delete this apporpriate  port number then program will generate random port number
	#portNum = 2555 # setting back to an appropraite interval
	
	print "\nRandom portNum Range is between 1333 to 11111 "
	print "You can change MAXPORT and MINPORT inside the  script"
	print "Random Port number is: ",portNum
	print "\n"

	app.run(host='penstemon.cs.engr.uky.edu',debug=False, port =portNum) # with using pen.cs.uky.edu  multi server
	
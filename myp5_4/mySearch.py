
##############################################################################
#Name : BINOD KATWAL                      					Date: 04/25/17
#Class : CS316 
#Project:  05 
##############################################################################

from flask import render_template, flash, redirect
from myp5_4 import app
from .myForms import AForm
import simplejson as json



"""def mySearch(a1, b1, c1):

    output = "my functions parameters are:  "+a1+" "+b1+" "+c1+"  !"
    return output """




# Main Function to Search the search record to put up records
#statFile is the FIle name that contains details of Runners
# Match is the function for What to  Match
#Value is the MatchValue(text)
#Stat is the stats section that we choose to find it's Max and MIN
#HighLow is the Max and min 
#################################################################################################
def mySearch(statFile, Match,Value, stat,highLow): 

#Display Information  To Check
    print "Inside mySearch()"
    print "stat file name =", statFile
    print "stat required =", stat
    print "what to match=", Match
    print "maxOrmin =", highLow
    print "Value to Match=", Value

    filetoOpen = 'myp5_4/static/'+str(statFile) #Get state files
	 # using Try and Except to check....
    try: 	
    	statFile = open(filetoOpen, 'r') 
    except IOError:
	print "Error: can\'t find ", statFile
	
	findMe = {"IOError"} #assign findMe error 
	return findMe #return 
    	
    else:	
    	contents = statFile.read() # read the file
    	statFile.close(); #close
    	control = json.loads(contents) #load

# Set temp as runners
    	temp = control['runners'] # Load the json file and get runners
    	findMe={}	 

		
	
	for index in range(len(temp)):	
		if temp[index].has_key(stat):	
			currStat = temp[index][stat] #"currStat" is array of the stat of all runners
			print "Testing!!!"
			break;
		else:	
			return findMe
    		print currStat
    		print temp[0]
		
   	

#If Users choice is "Nothing", what it does is matchValue and nothing will be ignore and move forward with stat
   	if Match == "Nothing":
		print " nothing"
		
		currStat = temp[0][stat] # Current stat

		# If max is selected, perform the code below	
		if 	highLow == "Max" :


			
    			# Check  all runnners 
   				for index in range(len(temp)):

   					# calling convertsecond Function to  convert time into second 
   						if ('.' in currStat == None):
   							 Convertsecond(currStat)
   							

   						#elif temp[index][stat] == None:
   							#print "length :",len(temp)
   							#continue

   						# WIll find Max 
						elif  temp[index][stat] > currStat : # temp is runners, all runners check < current stat
							findMe.clear() #clear
							findMe.update(temp[index]) # update information
							temp[index][stat]  = currStat #gets value
							#print "MA1"
					
							#
						elif temp[index][stat] == currStat : # temp is runners, all runners check > current stat
							findMe.clear()
							findMe.update(temp[index])	
							temp[index][stat] =  currStat 
							#print "MA2"
				return findMe #  return in the End of the loop

			
			
					
		#If user selcted Min, then Perform the code below
			
		elif highLow == "Min"  :
			try:
				currStat = temp[0][stat] # Current stats
    			# Check  all runnners 
   				for index in range(len(temp)):
   					if ('.' in currStat != None):
   							 Convertsecond(currStat)
   							 

   					
   					elif temp[index][stat] == None: # skeep if needed
   							
   							continue
					elif temp[index][stat] < currStat : # temp is runners, all runners check > current stat
						findMe.clear() #clear
						findMe.update(temp[index])#update info
						temp[index][stat] = currStat #get value
						#print "Mi2"
				
					 
					elif temp[index][stat] == currStat :# temp is runners, if in all runners check == current stat
						findMe.update(temp[index])
						temp[index][stat] = currStat 
						#print "Mi2"
				return findMe # return at the end of the loop
				 
			except:#display error
					print "Error: can't find "
					findMe = {"IOError"}
					return findMe
			


	# IF Users refuse to choose Nothing  and continue  searching records

	elif Match != "Nothing": # if matchValue doesn't equal Stat "Nothing"
			
		
		if 	highLow == "Max" : #Max
			try:
				currStat = temp[0][stat] # Current stats
    			# Check  all runnners 

   				for index in range(len(temp)): # loop starts
   				  
					# If max is selected, perform the code below
					if Value == temp[index][Match]:	
						
				 		if ('.' in currStat == None):
   							 Convertsecond(currStat)


						elif temp[index][stat] == None:
   							#print "length :",len(temp)
   							continue

						elif  temp[index][stat] > currStat : # temp is runners, all runners check < current stat
							findMe.clear()
							findMe.update(temp[index]) # update information
							temp[index][stat]  = currStat #get value
							#print "MA1"
					

						elif temp[index][stat] == currStat : # temp is runners, all runners check > current stat
							findMe.clear()
							findMe.update(temp[index])	
							temp[index][stat]  = currStat 
							#print "MA2"
				return findMe # Return at the end of the loop
					

			except : #Dipaly error
					print "Error: can't find "
					findMe = {"IOError"}
					return findMe
				
			#	If user selcted Min, then Perform the code below		
		elif highLow == 'Min' :
			
			try:
				currStat = temp[0][stat] # Current stats		
				#If user selcted Min, then Perform the code below
				for index in range(len(temp)):	# loop starts     
				
    			# Check  all runnners 
   				
   					if Value == temp[index][Match]: # if matched 
   						#print "hello"

   						if ('.' in currStat == None): # time convert to seconds
   							 Convertsecond(currStat)

   						
   						elif temp[index][stat] == None: # skip
   							#print "length :",len(temp)
   							continue

						elif temp[index][stat] < currStat : # temp is runners, all runners check > current stat
							findMe.clear()
							findMe.update(temp[index])
							currStat = temp[index][stat]
							#print "Mi2"
				
					 
						elif temp[index][stat] == currStat :# temp is runners, if in all runners check == current stat
							findMe.update(temp[index])
							currStat = temp[index][stat] 
							#print "Mi2"
				return findMe  # return at the end of the loop
					
		
			except : #Displays error
				print "Error: can't find "
				findMe = {"IOError"}
				return findMe
	


# END of the mySearch function 

############################################################################################




#  Function will  Convert time into Seconds
def convTimeToSeconds(x):
	rc = strpos(x, ".")

	if (rc == None): 
    	# no "."
    		newstring = x;
    	else: 
    		newstring =substr(x,0, rc)

   	tarray = explode(":", newstring)

    	if count(tarray) > 3 | count(tarray < 2):

    		print "Error on string conversion: ".newstring 
    		return -1; # displays

    	if (count(tarray) == 3):

			seconds = tarray[0]*3600+tarray[1]*60+tarray[2]
    			return seconds
   			
    	if (count(tarray) == 2):

   			seconds = tarray[0]*60+tarray[1];

    			return seconds
    			

#Function will convert time to seconds
def Convertsecond(s): 
	rc = "."  in s != None # if doesnt equal to None

	if rc == None: # if none
		print "hey" 
    		#newstring = 
    		print "hey2"
		l = map(int,s.split(":"))
		return sum(n * sec for n, sec in zip(l[::-1], (1, 60, 3600)))
	
    


   
# Search-Race1





Description:

The Purpose of the project is to replicate the basic PHP web application from Project 4 using the Flask framework.This Flask application will accept search 				parameters via a web form and perform basic searches on files local to the 		webserver. Searches will involve JSON objects stored in those files.

In order to run the Server, first you have to execute hw4.py by command ./hw4.py 	and it accepts 3 parameters of webserver address, port number, and debug mode 	and  will call folder myp5_4 then import app then  _init_.py will import Flask 	 from flash, config app then  import views.py

index() simply renders the index.html template (in the myp5_4/templates folder).
search() renders the search.html template.  This template includes a form.
You will note that some flask "magic" is present.  You'll see flask syntax
in the form of {} (braces).  These are directives to the flask module to 
include other content (based on the tags used).

Views.py is the main part  where it routes the application by parsing the url, 	we hae defined multiple urls in order to perform the program.
The function search() by "/search" will include Get and Post method to get data from different files. the function will make an instant form class, form will inherited python form class, handles the information for search criteria in the search page.Form will look for .json files inside static folders  and if files aren't found, program will call error.html then throw an IOError otherwise will extracts each stat's file anme and stats types form the files. if there is any errors in the program, program will goes to conditions and calls mySearch() funciton from mySearch.py.

mySearch() will try to access the stat file as one of the argument.If the file 	is not found, it will throw error "IOError" and throws error string "findme" 	and if the file content is found then it will make nested object with  will 	json.load() class method. then It will perform the functionlities as per 		the  your selection of Max and min in search criteria.Then, program will go 	over all conditional statements, In conitional statement, it will  look at  	your selction of the "stattosearch", depending on if your selction is 	"		nothing" or not,  the program will go over all conditional statements.




Compilation:

1) To run the program:	./hw4.py
- as you run it, you will get inform about where in the  webserver information(http://penstemon.cs.engr.uky.edu:8888/)  or you can look at hw.py file where information is provided.

As we compile hw4.py file, This file will import folder "myp5_4".

Inside myp5_4:
There are many files and folders.
Files are  1)__init__.py 2)myForms.py 3)mySearch.py 4)views.py 
And there are two folders, they are 1) static and 2) templates

1) Static folder- it contains all .json files use in the program. they are Races.json, 						2016_Gobbler.json and 2016_Ironhorse.json 
2) templates floder- it contains all .html files use in the program.they are base.html, 					error.html,index.html, result.html, search1.html and search1.html

2) Program will generate different portNum depending on your range of Max and MIn port 		therefore, its essestial to use right Port number to access then.
For exmaple: Go to web server : http://penstemon.cs.engr.uky.edu:8888/

The web server will display search Record  html page  from file "search1.html"
As per your search information,it will  go to view.py then collect data from .json file by using  search mySearch.py  and other files. if the search record is match, it it will take us to result.html file and displays Found search records or else it will use error. html to produce error message. Example of found records as follows:-



If you have selected:
stat file = 2016_Gobbler.json
whattomatch= Nothing
stat to search = Place
maxOrmin = Max
Value to match = 

Then you will get result inside the table is:

Found Records:
FinishTime	3:17:45.01
Name	Misty Pope
Gender	F
Age	42
Pace	15:06
Place	282
AgePlace	37
Hometown	Lexington
AgeCategory	F 40-44





# Search-Race clear
# Search-Race1

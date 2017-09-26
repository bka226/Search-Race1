##############################################################################
#Name : BINOD KATWAL                                        Date: 04/25/17
#Class : CS316 
#Project:  05 
##############################################################################


from flask import render_template, flash, redirect, request, url_for
import simplejson as json

from myp5_4 import app
from .myForms import AForm
from .mySearch import mySearch

# Home page, render  index.html from templates
@app.route('/')
def index():
    return render_template('index.html',title='MyP5_4')


"""
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = AForm()

    if form.validate_on_submit():
        #aPage = mySearch(form.A.data, form.B.data, form.C.data);

        aPage = mySearch(request.form['fileToSearch'],request.form['statToSearch'], request.form['functWanted']);
        flash(aPage)
        return redirect('/')
    return render_template('search.html',title='Search', form=form)
#    return "In, search"

"""
#Ironhorse stat
@app.route('/Ironhorse', methods=['GET', 'POST'])
def Ironhorse():
    

        jsonFile = open('app/static/2016_Ironhorse.json')
        raceData = jsonFile.read()
    
        print " can't find stat file"
    

    # You should check for JSON errors....maybe try/except ?
    
        raceJson = json.loads(raceData)
        theRaces = raceJson['Races']


    

# Main route: This Route will get users request, renders html templates and display the records
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = AForm()
    # if any errors found
    if form.Err == True:
        error = 'Races.json does not exist!' 
        return redirect(url_for('Err', err = error))   

    else: # else           
        if request.method == 'POST':
            answer = mySearch(request.form['fileToSearch'], request.form['WhatToMatch'],request.form['matchValue'],request.form['statToSearch'],request.form['maxOrmin']);
            # if any below issue, print redirect url
            if answer == {}:
                error = 'Requested information does not exists !!!'  
        
                return redirect(url_for('Err', err=error))

            elif answer == {"IOError"}:
                error = "Stat file not found!" 
                return redirect(url_for('Err', err=error))

            #else
            else:
                #if not found value
                if (answer is None ):
                    flash(" Search Record is not Found!!!")
                    #return redirect('/notused')
                    return redirect('/')
                else:
                    #if found then render 
                    return render_template('result.html', form=answer)
                    
                    flash(answer)
                    return redirect('/')
    #debug: Print
        print form.fileToSearch
        print form.statToSearch
        print form.WhatToMatch
        print form.maxOrmin  
        return render_template('search1.html',title='Search',form=form) # render 



# this route will calls error.html and displays error
@app.route('/error/<err>')
def Err(err):

    return render_template('error.html', error = err)




# This Route will will check users requests and display results

@app.route('/Gobbler', methods=['GET', 'POST'])
def Gobbler():
    form = AForm()
    if form.Err == True:
        error = 'Races.json does not exist!' 
        return redirect(url_for('Err', err = error))   

    else:           
        if request.method == 'POST':
            answer = mySearch(request.form['fileToSearch'], request.form['WhatToMatch'],request.form['matchValue'],request.form['statToSearch'],request.form['maxOrmin']);
            if answer == {}:
                error = 'Requested information does not exists !!!'  
        
                return redirect(url_for('Err', err=error))

            elif answer == {"IOError"}:
                error = "Stat file not found!" 
                return redirect(url_for('Err', err=error))

            
            else:

                if (answer is None ):
                    flash(" Search Record is not Found!!!")
                    #return redirect('/notused')
                    return redirect('/')
                else:
                    return render_template('result.html', form=answer)
                    flash(answer)
                    return redirect('/')
    #debug:
        print form.fileToSearch
        print form.statToSearch
        print form.WhatToMatch
        print form.maxOrmin  
        return render_template('search1.html',title='Search',form=form)
    

  


    



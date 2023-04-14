#!/usr/bin/env python
from flask import Flask, request, render_template
import os, random
from os import system
from flask_cors import CORS, cross_origin
from flask import jsonify
from flask import request
from flask import render_template, redirect, url_for, request
import socket
import webbrowser

from shutil import move
import json, uuid
import sys







#############################################
#   LIBRARY IMPORT
#############################################

#   APPLICATION ROOT
parent_path = os.path.split(os.path.dirname(  os.path.realpath(__file__) ))[0] + '/'
this_app_path = os.path.dirname(  os.path.realpath(__file__) )
sys.path.append(parent_path)

#   IMPORT LIBRARIES
from libraries.files_and_folders import folders
from libraries.files_and_folders import CleanFolder
from libraries.files_and_folders import CopyFile
from libraries.files_and_folders import CopyFileAndRename
import libraries.core as core
from libraries.core import StartApp
from libraries.database_connector import DumpAndCreateDatabase
from libraries.database_connector import TestDatabase
import libraries.console as console
from libraries.database_connector import DumpAndCreateAccountsDatabase

#   RETURN TO APP PATH
sys.path.append(this_app_path)

#############################################
#############################################
#############################################


#   CMD TITLE FOR AUTO CLOSING
system("title web_ui")


#   SERVER SETUP
server_port = 1001

#   DATA OUTPUT
data_output = ""
parent_path = os.path.split(os.path.dirname(  os.path.realpath(__file__) ))[0] + '/'


#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#==============[SYSTEM START]==============#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#


#   CREATE FLASK APP
app = Flask(__name__)



#############################################
#   DISABLE THE CACHE FOR LIVE JSON RELOADING
#############################################
@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
#############################################
#############################################
#############################################



#############################################
#   SETUP FLASK LOGIN
#############################################

import flask_login

app.secret_key = 'super secret string'  # Change this!

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# Our mock database.
users = {'loggy': {'password': 'idsidsidsids'}}

class User(flask_login.UserMixin):
    pass

#############################################
#############################################
#############################################


#############################################
#   USER SESSIONS AND ACCOUNTS
#############################################

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='username'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return redirect('/')
    #return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect('/login')
#############################################
#############################################
#############################################



#############################################
#   CORE PAGES
#############################################

#   HOME
@app.route('/')
@flask_login.login_required
def home():
    return render_template("home.html", data_output=data_output)

#   PROCESS: VIRTUAL FTP IMAGE DROP
@app.route('/process/virtual_ftp_image_drop', methods=["GET", "POST"])
@flask_login.login_required
def virtual_ftp_image_drop():
    global data_output

    test_img_filename = folders["test-grab-images"] + random.choice( os.listdir( folders["test-grab-images"] ) )


    CopyFileAndRename(test_img_filename, folders["ftp_image_drop"], core.Timestamp() + '.jpg')
    
    data_output = "Dropped Virtual FTP Image Into Loggy Core = " + test_img_filename

    return redirect('/')





#   PROCESS: START IMAGE PROCESSOR
@app.route('/process/image_processor', methods=["GET", "POST"])
@flask_login.login_required
def image_processor():
    global data_output
    
    app_path = parent_path + 'image_processor/'
    
    data_output = "Starting System Core - " + app_path + ' - image_processor.bat'

    StartApp(app_path,  "image_processor.bat")
    return redirect('/')



#   PROCESS: START GRAB PROCESSOR
@app.route('/process/grab_processor', methods=["GET", "POST"])
@flask_login.login_required
def grab_processor():
    global data_output
    
    app_path = parent_path + 'grab_processor/'
    
    data_output = "Dropped Virtual FTP Image Into Loggy Core - " + app_path + ' - grab_processor.bat'

    StartApp(app_path,  "grab_processor.bat")
    return redirect('/')


#   PROCESS: START COUNT THINGS
@app.route('/process/count_things', methods=["GET", "POST"])
@flask_login.login_required
def count_things():
    global data_output
    
    data_output = "Killing & Starting Count Things."
    os.system('TASKKILL /F /IM "CountThings from Photos.exe"')
    os.startfile('"C:\Program Files\Dynamic Ventures, Inc\CountThings from Photos (64-bit)\CountThings from Photos.exe"')

    return redirect('/')


#   PROCESS: CLEAN FOLDER = DROP
@app.route('/process/clean_folder_image_drop', methods=["GET", "POST"])
@flask_login.login_required
def clean_folder_image_drop():
    global data_output
    
    data_output = "Cleaning Folder [Image Drop]"
    CleanFolder( folders["count_things_image_drop"] )
    return redirect('/')



#   PROCESS: CLEAN FOLDER = OUTPUT
@app.route('/process/clean_folders_count_output', methods=["GET", "POST"])
@flask_login.login_required
def clean_folders_count_output():
    global data_output
    
    data_output = "Cleaning Folders [Count Output]"
    CleanFolder( folders["count_things_input_photos"] )
    CleanFolder( folders["count_things_detections"] )
    return redirect('/')

#   PROCESS: CLEAN FOLDER = PROCESSING
@app.route('/process/clean_folders_count_processing', methods=["GET", "POST"])
@flask_login.login_required
def clean_folders_count_processing():
    global data_output
    
    data_output = "Cleaning Folders [Count Processing]"
    CleanFolder( folders["count_things_processing"] )
    return redirect('/')
    


#   PROCESS: 
@app.route('/process/clean_accounts_db', methods=["GET", "POST"])
@flask_login.login_required
def clean_accounts_db():
    global data_output
    
    data_output = "Cleaning User Accounts Database"

    DumpAndCreateAccountsDatabase()

    return redirect('/')  

#   PROCESS: 
@app.route('/process/clean_db', methods=["GET", "POST"])
@flask_login.login_required
def clean_db():
    global data_output
    
    console.PrintStatement("Cleaning Logistics Database")

    data_output = "Cleaning Logistics Database"

    DumpAndCreateDatabase()

    return redirect('/')  


#   PROCESS: 
@app.route('/process/test_db', methods=["GET", "POST"])
@flask_login.login_required
def test_db():
    global data_output
    
    console.PrintStatement("Testing Database")

    data_output = "Testing Database"

    TestDatabase()

    return redirect('/')  

#############################################
#############################################
#############################################


#############################################
#   COMMANDS
#############################################



#############################################
#############################################
#############################################






#############################################
#   SYSTEM CORE
#############################################

if __name__ == '__main__':

    this_ip_address = socket.gethostbyname(socket.gethostname())
    url = "http://" + str(this_ip_address) + ":" + str(server_port)

    app.debug = True
    app.run(host = this_ip_address,port=server_port)

#############################################
#############################################
#############################################




#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#===============[SYSTEM END]===============#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
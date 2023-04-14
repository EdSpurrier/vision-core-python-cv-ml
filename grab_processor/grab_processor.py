#!/usr/bin/env python

from os import system
import os
import sys
import getopt


#   CMD TITLE FOR AUTO CLOSING
system("title grab_processor")


#############################################
#   LIBRARY IMPORT
#############################################

#   APPLICATION ROOT
parent_path = os.path.split(os.path.dirname(  os.path.realpath(__file__) ))[0] + '/'
this_app_path = os.path.dirname(  os.path.realpath(__file__) )
sys.path.append(parent_path)

#   IMPORT LIBRARIES
import libraries.database_connector as db
from libraries.files_and_folders import folders
from libraries.files_and_folders import urls
from libraries.files_and_folders import MoveFileAndRename
from libraries.files_and_folders import DeleteFile
from libraries.files_and_folders import CheckFileExists
from libraries.files_and_folders import StripFileName
from libraries.files_and_folders import StripFileNameBeforeChar
from libraries.files_and_folders import CheckFileExistsNow

import libraries.core as core
import libraries.console as console
import libraries.ftp_uploader as ftp





#   RETURN TO APP PATH
sys.path.append(this_app_path)

#############################################
#############################################
#############################################



ftp_image_url = None
working_process_name = None

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#==============[SYSTEM START]==============#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

import ntpath
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def ProcessGrab(grab_file):
    
    global working_process_name

    working_image_file_url = folders["count_things_input_photos"] + os.path.splitext( str( path_leaf(grab_file) ) )[0] + '.jpg'



    console.Print("<Created> Timestamp Filename = " + working_process_name)


    if CheckFileExists(working_image_file_url):
        MoveFileAndRename(working_image_file_url, folders["count_things_processing"], working_process_name + '.jpg')

    if CheckFileExists(grab_file):
        MoveFileAndRename(grab_file, folders["count_things_processing"], working_process_name + '.json')

    processed_image_file_url = folders["count_things_processing"] + working_process_name + '.jpg'



    original_image_drop_file = os.path.splitext( str( path_leaf(grab_file) ) )[0]
    original_image_drop_file_split = original_image_drop_file.split('_')
    original_image_drop_file = original_image_drop_file_split[0]

    if CheckFileExistsNow(folders["ftp_image_drop"] + '/' + original_image_drop_file + '.jpg'):
        DeleteFile( folders["ftp_image_drop"] + '/' + original_image_drop_file + '.jpg', False )
    
    if CheckFileExistsNow(folders["count_things_image_drop"] + '/' + original_image_drop_file + '.jpg'):
        DeleteFile( folders["count_things_image_drop"] + '/' + original_image_drop_file + '.jpg', False )


    if CheckFileExists(processed_image_file_url):


        if ftp.UploadFileFTP('grabs/', working_process_name + ".jpg", processed_image_file_url):

            grab_image_url = urls["grabs_url"] + working_process_name + ".jpg"

            console.Print("Successfully Uploaded = " + grab_image_url)
            

            if db.CreateNewGrab( working_process_name,  grab_image_url ) == True:

                console.PrintStatement("Added Grab To Database")


                core.StartApp( folders["log_processor"], "log_processor.bat " + working_process_name )
                print("log_processor.bat " + working_process_name)


                system("title grab_processor")


            else:

                console.PrintError("Error Adding Grab To Database")
        
        else:
            console.PrintError("FTP Upload Error")


    

    core.CheckCountThingsAndKill()



    sys.exit()











""" 

    w = Watcher()
    w.run() """






#######################
#   WATCH DOG SYSTEM
#######################
from watchdog.observers import Observer
from watchdog.events import (
    PatternMatchingEventHandler, FileModifiedEvent,
    FileCreatedEvent, FileSystemEventHandler)


class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):
        print('Watching DIR for changes = ' + folders["count_things_detections"])
        event_handler = Handler()
        self.observer.schedule(event_handler, path=folders["count_things_detections"])
        self.observer.daemon = False
        self.observer.start()
        self.observer.join()

    def kill(self):
        self.observer.stop()



class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        global working_process_name

        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            console.Print('Received created event - %s.' % event.src_path)

            

            ftp_id = StripFileName(ftp_image_url)
            event_id = StripFileNameBeforeChar(event.src_path, "_")

            console.Print('checking_url = ' + ftp_id + " | event.src_path = " + event_id)
            if str(ftp_id) == str(event_id):
                working_process_name = event_id
                ProcessGrab(event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print('Received modified event - %s.' % event.src_path)



#######################
#######################
#######################








#############################################
#   SYSTEM CORE
#############################################


def main(argv):

    global ftp_image_url

    try:
        opts, args = getopt.getopt(argv, "ftp_image_url")

    except getopt.GetoptError:
        console.Print('ERROR = grab_processor.py <ftp_image_url>')
        sys.exit(2)

    ftp_image_url = args[0]

    #ProcessGrab(ftp_image_url)

    w = Watcher()
    w.run()
    

            
if __name__ == "__main__":
   main(sys.argv[1:]) 


#############################################
#############################################
#############################################


#############################################
#   OLD SYSTEM CORE
#############################################


""" if __name__ == '__main__':

    w = Watcher()
    w.run() """



#############################################
#############################################
#############################################




#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#===============[SYSTEM END]===============#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
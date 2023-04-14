#!/usr/bin/env python

from os import system
import os
import sys


#   CMD TITLE FOR AUTO CLOSING
system("title image_processor")


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
from libraries.files_and_folders import CleanFolder
from libraries.files_and_folders import FindFilesWithExtension


import libraries.core as core
import libraries.console as console

import libraries.ftp_uploader as ftp





#   RETURN TO APP PATH
sys.path.append(this_app_path)

#############################################
#############################################
#############################################




#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#==============[SYSTEM START]==============#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

import ntpath
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def ProcessFTPImageDrop(ftp_image_file):
    console.NewProcess('Processing Uploaded Image [' + ftp_image_file + "]")


    working_filename = core.Timestamp()


    #core.StartApp( folders["count_things_app"], 'count_things.bat ' + ftp_image_file + '' )


    console.PrintAlert("Running Windows Based CountThings App")
    #CleanFolder(folders["count_things_image_drop"])

    if CheckFileExists( folders["count_things_image_drop"] ):
        core.StartAndKillCountThings()
        MoveFileAndRename(ftp_image_file, folders["count_things_image_drop"], working_filename + '.jpg')

    

    core.StartApp( folders["grab_processor"], 'grab_processor.bat "' + working_filename + '"' )
    






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
        print('Watching DIR for changes = ' + folders["ftp_image_drop"])
        event_handler = Handler()
        self.observer.schedule(event_handler, path=folders["ftp_image_drop"])
        self.observer.daemon = False
        self.observer.start()
        self.observer.join()

    def kill(self):
        self.observer.stop()



class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        #global working_filename

        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            console.Print('Received created event - %s.' % event.src_path)

            
            


            ProcessFTPImageDrop(event.src_path)
            

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            console.Print('Received modified event - %s.' % event.src_path)



#######################
#######################
#######################











#############################################
#   SYSTEM CORE
#############################################


if __name__ == '__main__':
    console.NewProcess("Checking For Unprocessed FTP Uploads")


    files_to_process = FindFilesWithExtension(folders["ftp_image_drop"], "jpg")
    for file_to_process in files_to_process:
        ProcessFTPImageDrop(file_to_process)

    console.NewProcess("Watching FTP Uploads")



    w = Watcher()
    w.run()



#############################################
#############################################
#############################################




#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#===============[SYSTEM END]===============#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
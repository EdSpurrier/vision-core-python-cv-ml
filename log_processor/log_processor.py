#!/usr/bin/env python

from os import system
import os
import sys
import getopt




#   JSON
import json, uuid

#   CMD TITLE FOR AUTO CLOSING
system("title log_processor")



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
from libraries.files_and_folders import CreateDirectory
from libraries.files_and_folders import DeleteDirectory
from libraries.files_and_folders import CheckFileExists
from libraries.files_and_folders import DeleteFile
import libraries.core as core
import libraries.console as console
import libraries.ftp_uploader as ftp
from libraries.image_cut import CutOutLogImage
from libraries.barcode_scanner import ProcessBarcode

from libraries.log_calculations import CalculateDiameter
from libraries.log_calculations import CalculateJAS
from libraries.log_calculations import CalculateCBM


#   RETURN TO APP PATH
sys.path.append(this_app_path)

#############################################
#############################################
#############################################







#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#==============[SYSTEM START]==============#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#


#   LOG DATA
log_data_json = []
log_data_pre = []
log_data = []
processed_log_data = []

grab_unique_id = None
working_file_name = None
output_working_file_name = None
json_file = None
img_file = None
output_path = None


#   SETTINGS
safety_margin = 1.1
real_label_width = 80

###########################
#   EXTRACT LOG META DATA
###########################
def ProcessLogs():
    global log_data
    global log_data_json
    global output_path

    global working_file_name
    global output_working_file_name
    global json_file
    global img_file

    console.NewProcess("Starting Log Processor [grab_unique_id = " + grab_unique_id + "]")


    output_path = folders["log_processing"] + grab_unique_id + "/"
    output_working_file_name = output_path + grab_unique_id
    working_file_name = folders["count_things_processing"] + grab_unique_id
    
    json_file = working_file_name +".json"
    img_file = working_file_name +".jpg"

    CreateDirectory(output_path)
    
    console.Print("Processing File = " + json_file)


    with open(json_file, 'r') as f:
        log_data_json = json.load(f)

    count_non_logs = 0
    count_logs = 0

    for log_line in log_data_json:
        if log_line["Label"] != '':

            console.NewProcess("Processing Log Line - " + log_line["Label"])

            if CheckFileExists( output_path ):
                log_img_file = CutOutLog(log_line)[0]


            #   IMAGE FILES NAMES FOR UPLOADING
            log_image_file_name = grab_unique_id + "_" + log_line["Label"] + ".jpg"
            barcode_image_file_name = grab_unique_id + "_" + log_line["Label"] + "_barcode.jpg"

            barcode, label_width, output_img_barcode_file = FindBarcode(log_img_file, output_path + barcode_image_file_name)




            if barcode != 0:
                actual_diameter = CalculateDiameter(label_width, real_label_width, log_line["Width_Pixels"])     
                jas_diameter = CalculateJAS(actual_diameter)     


                log_barcode_image_url = "None"
                log_image_url = "None"


                if ftp.UploadFileFTP('logs/', barcode_image_file_name, output_img_barcode_file):
                    log_barcode_image_url = urls["logs_url"] + barcode_image_file_name
                           
                if ftp.UploadFileFTP('logs/', log_image_file_name, log_img_file):
                    log_image_url = urls["logs_url"] + log_image_file_name


                log_line_data = {
                    "log_id": str(barcode),
                    "log_img_url": str(log_barcode_image_url),
                    "barcode_img_url": str(log_image_url),
                    "grab_unique_id": str(grab_unique_id),
                    "grab_position_x": str(log_line["X"]),
                    "grab_position_y": str(log_line["Y"]),
                    "grab_width": str(log_line["Width_Pixels"]),
                    "grab_height": str(log_line["Height_Pixels"]),
                    "actual_diameter": str(actual_diameter),
                    "jas_diameter": str(jas_diameter),
                    "jas_cbm": str(0.00),
                }

                db.CreateNewLog(log_line_data)

                

            else:
                if CheckFileExists( log_img_file ):
                    DeleteFile(log_img_file, False)
            
            count_logs += 1


        else:
            count_non_logs += 1


    console.NewProcess("Printing Log Lines")
    for log_line in log_data:
        console.Print( str(log_line) )
        console.ClearLine()

    
    console.Print("Log Found => " + str(count_logs) )
    console.Print("Log (Non-Log) => " + str(count_non_logs) )
    
    
    CleanUp()
    core.CheckCountThingsAndKill()

###########################
###########################
###########################



#######################
#   CUT OUT LOG
#######################

def CutOutLog(log_line_data):

    return CutOutLogImage(img_file, output_working_file_name, log_line_data["Label"], log_line_data["X"], log_line_data["Y"], log_line_data["Width_Pixels"], log_line_data["Height_Pixels"], safety_margin), 

#######################
#######################
#######################



#######################
#   FIND BARCODE
#######################

def FindBarcode(inputName_Path, outputName_Path):


    return ProcessBarcode(inputName_Path, outputName_Path)


#######################
#######################
#######################



#######################
#   CLEAN UP
#######################
def CleanUp():
    DeleteDirectory(output_path)
    DeleteFile(json_file)
    DeleteFile(img_file)
    


#######################
#######################
#######################







#############################################
#   SYSTEM CORE
#############################################


def main(argv):

    global grab_unique_id

    try:
        opts, args = getopt.getopt(argv,"grab_unique_id")

    except getopt.GetoptError:
        print('ERROR = ProcessCount.py <grab_unique_id>')
        sys.exit(2)

    grab_unique_id = args[0]
    

    ProcessLogs()

    system("title log_processor_finished")

    #system(' taskkill /fi "WindowTitle eq log_processor_finished" ')
    #sys.exit()

            
if __name__ == "__main__":
   main(sys.argv[1:]) 


#############################################
#############################################
#############################################




#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#
#===============[SYSTEM END]===============#
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
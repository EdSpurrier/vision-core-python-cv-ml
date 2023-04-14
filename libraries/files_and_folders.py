import os
import sys
import time

#   FILE MANAGEMENT
import shutil
from shutil import move
import send2trash
import pathlib
import ntpath
import glob


#   APPLICATION ROOT
sys.path.append(os.path.split(os.path.dirname(  os.path.realpath(__file__) ))[0] + '/')

#   IMPORT LIBRARIES
import libraries.console as console


console.PrintImport("files_and_folders.py")

parent_path = os.path.split(os.path.dirname(  os.path.realpath(__file__) ))[0] + '/'

parent_path = parent_path.replace("\\", "/")


#   DIRECTORIES
folders = {
    "parent_path" : parent_path,
    "count_things_detections" : parent_path + "count_things/count_output/Detections/",
    "count_things_input_photos" : parent_path + "count_things/count_output/InputPhotos/",
    "count_things_image_drop" : parent_path + "count_things/image_drop/",
    "count_things_processing" : parent_path + "count_things/processing/",
    "log_processing" : parent_path + "log_processing/",
    "test-grab-images" : parent_path + "test-grab-images/",
    "online_grab_image_repo" :  parent_path + "test-image-repo/",
    "log_processor" :  parent_path + "log_processor/",
    "grab_processor" :  parent_path + "grab_processor/",
    "assets" : parent_path + "assets/",
    "ftp_image_drop" : parent_path + "ftp_image_drop/",
    "count_things_app" : parent_path + "count_things/count_things_app/",
    "internal_server_ftp_folder" : "C:/wamp64/www/loggy/ftp/",
}


urls = {
    "grabs_url" : "http://lumigear.net/loggy/grabs/",
    "logs_url" : "http://lumigear.net/loggy/logs/",
}


#######################
#   RETURN ALL FILES OF EXTENSION TYPE
#######################
def FindFilesWithExtension(folder_path, file_extension):
    console.Print("Searching Folder [" + folder_path + "] For Files => *." + file_extension )
    return glob.glob(folder_path + "*." + file_extension)

#######################
#   CHECK FILE EXISTS
#######################
def CheckFileExists(file_path):

    time_to_wait = 50
    time_counter = 0
    while not os.path.exists(file_path):
        console.PrintDebug("Waiting For File To Exist = " + file_path + " Status: " + str(os.path.exists(file_path)) )
        
        time.sleep(1)
        time_counter += 1
        if time_counter > time_to_wait:
            break
            console.PrintError("File Time Out = " + file_path)
            sys.exit()

    console.PrintDebug("Found = " + file_path)

    return True


#######################
#   CHECK FILE EXISTS
#######################
def CheckFileExistsNow(file_path):

    if os.path.exists(file_path):
        console.PrintDebug("Found = " + file_path)
        return True
    else:
        return False





#######################
#   STRIP FILE TO NAME NO EXT
#######################


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def StripFileName(file_path):
    return os.path.splitext( str( path_leaf(file_path) ) )[0]


def StripFileNameBeforeChar(file_path, char_to_search):
    stripped_file_name = os.path.splitext( str( path_leaf(file_path) ) )[0]
    stripped_file_name_split = stripped_file_name.split( char_to_search )


    return stripped_file_name_split[0]

#######################
#   CLEAN FOLDER
#######################
def CleanFolder(folder_path):
    print("*******************************************")
    print("ALERT - Cleaning Folder [" + folder_path + "]")
    print("*******************************************")
    
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    
    pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True) 


#######################
#   COPY FILE
#######################
def CopyFile(input_file, output_path):
    print("*******************************************")
    print("ALERT - COPING FILE")
    print("[" + input_file + "] >>> [" + output_path + "]")
    print("*******************************************")
    
    shutil.copy(input_file, output_path)


#######################
#   COPY FILE & RENAME
#######################
def CopyFileAndRename(input_file, output_path, new_name):

    new_output_path = output_path + new_name
    print("*******************************************")
    print("ALERT - COPING FILE")
    print("[" + input_file + "] >>> [" + new_output_path + "]")
    print("*******************************************")
    
    shutil.copy(input_file, new_output_path)





#######################
#   MOVE FILE & RENAME
#######################
def MoveFileAndRename(input_file, output_path, new_name):

    new_output_path = output_path + new_name
    print("*******************************************")
    print("ALERT - MOVING FILE")
    print("[" + input_file + "] >>> [" + new_output_path + "]")
    print("*******************************************")
    
    shutil.move(input_file, new_output_path)

#######################
#   DELETE FILE
#######################
def DeleteFile(input_file, safe_delete = True):

    print("*******************************************")
    print("ALERT - DELETING FILE")
    print("[" + input_file + "]")
    print("*******************************************")

    os.unlink(input_file)


#######################
#   CREATE DIRECTORY
#######################
def CreateDirectory(folder_path):

    print("*******************************************")
    print("ALERT - CREATING DIRECTORY")
    print("[" + folder_path + "]")
    print("*******************************************")

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    
    pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True) 


#######################
#   DELETE DIRECTORY
#######################
def DeleteDirectory(folder_path):

    print("*******************************************")
    print("ALERT - DELETING DIRECTORY")
    print("[" + folder_path + "]")
    print("*******************************************")

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)

import arrow
import os
import sys


#   APPLICATION ROOT
sys.path.append(os.path.split(os.path.dirname(  os.path.realpath(__file__) ))[0] + '/')

#   IMPORT LIBRARIES
import libraries.console as console
from libraries.files_and_folders import FindFilesWithExtension
from libraries.files_and_folders import folders

console.PrintImport("core.py")


def Timestamp():
    return str(arrow.utcnow().timestamp)



def StartApp(app_dir, app_file):
    os.system('start cmd /k "cd "' + app_dir + '" && ' + app_file + '"')



def StartAndKillCountThings():
    KillCountThings()
    os.startfile('"C:\Program Files\Dynamic Ventures, Inc\CountThings from Photos (64-bit)\CountThings from Photos.exe"')       

def KillCountThings():
    os.system('TASKKILL /F /IM "CountThings from Photos.exe"')

def CheckCountThingsAndKill():
    console.PrintAlert("Checking Count Things Image Drop & Killing")
    files_waiting_for_process = FindFilesWithExtension(folders["count_things_image_drop"], "jpg")
    if len(files_waiting_for_process) == 0:
        console.PrintAlert("Killing Count Things")
        KillCountThings()
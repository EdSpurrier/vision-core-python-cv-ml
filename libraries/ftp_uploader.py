import ftplib 

import os
import sys
#   APPLICATION ROOT
sys.path.append(os.path.split(os.path.dirname(  os.path.realpath(__file__) ))[0] + '/')
#   IMPORT LIBRARIES
import libraries.console as console
from libraries.files_and_folders import CopyFile
from libraries.files_and_folders import folders
console.PrintImport("ftp_uploader.py")


password = "idsidsidsids"
username = "loggy@edspurrier.com"
server = "lumigear.net"

save_backup_on_server = True


def UploadFileFTP(destination_dir, file_name, file_location):
    console.PrintAlert("ALERT - Uploading File Via FTP [" + file_location + "] >> [" + destination_dir + "] = " + file_name)

    
    try:
        session = ftplib.FTP(server, username, password)
        file = open(file_location, 'rb')                  # file to send
        session.storbinary('STOR ' + destination_dir + file_name, file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()
        console.PrintSuccess("Successfully Uploaded")

        if save_backup_on_server == True:
            CopyFile(file_location, folders["internal_server_ftp_folder"] + destination_dir + file_name)

        return True
    except ftplib.all_errors as e:
        console.PrintError("FTP Upload Error", e) 
        return False  

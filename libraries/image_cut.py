import cv2
import os
import sys

#   APPLICATION ROOT
sys.path.append(os.path.split(os.path.dirname(  os.path.realpath(__file__) ))[0] + '/')

#   IMPORT LIBRARIES
import libraries.console as console
from libraries.files_and_folders import CheckFileExists

console.PrintImport("image_cut.py")




def CutOutLogImage(inputName_Path, outputName_Path, outputId, cutPositionX, cutPositionY, cutWidth, cutHeight, safetyMargin):

    input_width = cutWidth
    input_height = cutHeight

    cutout_width = (input_width * safetyMargin)/2
    cutout_height = (input_height * safetyMargin)/2

    left = cutPositionX - cutout_width
    top = cutPositionY - cutout_height

    right = cutPositionX + cutout_width
    bottom = cutPositionY + cutout_height

    img = cv2.imread(inputName_Path)

    crop_img = img[int(top):int(bottom), int(left):int(right)]

    outputName_Path = outputName_Path + "_" + outputId + ".jpg"

    if console.popupDebug == True:
        cv2.imshow("cropped", crop_img)
        cv2.waitKey(0)

    console.Print("Cropped Log id[" + outputId + "] - " +  outputName_Path)
    
    thisImage = cv2.imwrite( outputName_Path, crop_img )

    

    if thisImage:
        return outputName_Path

    
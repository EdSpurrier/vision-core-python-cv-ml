#!/usr/bin/env python
# Python 2/3 compatibility
import sys
PY3 = sys.version_info[0] == 3
if PY3:
    xrange = range
import numpy as np
import cv2 as cv
from scipy import ndimage
import time
import math
from pyzbar.pyzbar import decode
from math import atan2,degrees

import ntpath
import getopt
import json, uuid
from shutil import move
import os



#   APPLICATION ROOT
sys.path.append(os.path.split(os.path.dirname(  os.path.realpath(__file__) ))[0] + '/')
#   IMPORT LIBRARIES
import libraries.console as console

console.PrintImport("barcode_scanner.py")




#   BARCODE READ SIZE
widthmax = 300
heightmax = 300
widthMin = 60
heightMin = 60



def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def GetAngleOfLineBetweenTwoPoints(p1x, p1y, p2x, p2y):
    xDiff = p2x - p1x
    yDiff = p2y - p1y
    return degrees(atan2(yDiff, xDiff))


def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_squares(img):
    img = cv.GaussianBlur(img, (5, 5), 0)
    squares = []
    for gray in cv.split(img):
        for thrs in xrange(0, 255, 26):
            if thrs == 0:
                bin = cv.Canny(gray, 0, 50, apertureSize=5)
                bin = cv.dilate(bin, None)
            else:
                _retval, bin = cv.threshold(gray, thrs, 255, cv.THRESH_BINARY)
            contours, _hierarchy = cv.findContours(bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                rect = cv.minAreaRect(cnt)       #I have used min Area rect for better result
                width = rect[1][0]
                height = rect[1][1]

                if (width<widthmax) and (height <heightmax) and (width >= widthMin) and (height > heightMin):
                    cnt_len = cv.arcLength(cnt, True)
                    cnt = cv.approxPolyDP(cnt, 0.02*cnt_len, True)
                    if len(cnt) == 4 and cv.contourArea(cnt) > 1000 and cv.isContourConvex(cnt):
                        cnt = cnt.reshape(-1, 2)
                        max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                        if max_cos < 0.1:
                            squares.append(cnt)
    return squares

        
# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 1)
 
    # Display results
    return im

def Search_number_String(String):
    index_list = []
    del index_list[:]
    for i, x in enumerate(String):
        if x.isdigit() == True:
            index_list.append(i)
    start = index_list[0]
    end = index_list[-1] + 1
    number = String[start:end]
    return number

def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

def ProcessBarcode(inputName_Path, outputName_Path):
    from glob import glob
    
    console.PrintDebug(inputName_Path)

    img = cv.imread(inputName_Path)


    square_find_img = img
    
    squares = find_squares(square_find_img)


    barcodeFound = False
    barcode = 0

    console.ClearLine()
    console.PrintStatement("Initiated Scan For Barcode")


    for sqr in squares:
        #img = cv.line(img, (sqr[0][0], sqr[0][1]), (sqr[1][0], sqr[1][1]), (0,0,255), 1)

        

        #rotation angle in degree
        #rotatedImg = ndimage.rotate(img, currentRotation)

        safetyMargin = 0
 

        minX = [sqr[0][0], sqr[1][0], sqr[2][0], sqr[3][0]]
        minY = [sqr[0][1], sqr[1][1], sqr[2][1], sqr[3][1]]

        #print("min value element : ", min(minX) )
        #print("min value element : ", min(minY) )

        maxX = [sqr[0][0], sqr[1][0], sqr[2][0], sqr[3][0]]
        maxY = [sqr[0][1], sqr[1][1], sqr[2][1], sqr[3][1]]

        console.PrintDebug( str(sqr) )


        # GET TOP LEFT POINT

        minX_1 = min(minX)
        minX_2 = second_smallest(minX)
        
        console.PrintDebug('MinX - 1 = ' + str(minX_1) )
        console.PrintDebug('MinX - 2 = ' + str(minX_2) )

        topLeftPoint = []

        pointsToCheck = []

        for point in sqr:
            if point[0] == minX_1:
                pointsToCheck.append(point)

            elif point[0] == minX_2:
                pointsToCheck.append(point)

        minY_leftPoint = min([pointsToCheck[0][1], pointsToCheck[1][1]])

        console.PrintDebug('Top Points' + str(pointsToCheck) )

        console.PrintDebug('Min Y = ' + str(minY_leftPoint) )

        for point in pointsToCheck:
            if point[1] == minY_leftPoint:
                topLeftPoint = point

        console.PrintDebug('Top Left Point:' + str(topLeftPoint) )
        # >>>>>>>>>>>>>>>>>>>>>




        # GET TOP RIGHT POINT
        minY_1 = min(minY)
        minY_2 = second_smallest(minY)
        console.PrintDebug('MinY - 1 = ' + str(minY_1) )
        console.PrintDebug('MinY - 2 = ' + str(minY_2) )


        topRightPoint = []

        pointsToCheck = []
        
            
        for point in sqr:
            if point[1] == minY_1:
                pointsToCheck.append(point)

            elif point[1] == minY_2:
                pointsToCheck.append(point)

        minY_rightPoint = []

        console.PrintDebug('Comparing: ' + str(pointsToCheck[0][0]) + ' == ' + str(topLeftPoint[0]))
        console.PrintDebug('Then Comparing: ' + str(pointsToCheck[1][0]) + ' == ' + str(topLeftPoint[0]))

        if pointsToCheck[0][0] == topLeftPoint[0]:
            topRightPoint = pointsToCheck[1]
        elif pointsToCheck[1][0] == topLeftPoint[1]:
            topRightPoint = pointsToCheck[0]
        else:
            minY_rightPoint = min([pointsToCheck[0][1], pointsToCheck[1][1]])
            for point in pointsToCheck:
                if point[1] == minY_rightPoint:
                    topRightPoint = point

 
        
        console.PrintDebug('Top Points' + str(pointsToCheck) )

        console.PrintDebug('Min Y = ' + str(minY_rightPoint) )

        console.PrintDebug('Top Right Point: ' + str(topRightPoint) )
        # >>>>>>>>>>>>>>>>>>>>>


        console.PrintDebug( str(topLeftPoint) + ":" + str(topRightPoint) )

        rotatedImg = img

        if console.popupDebug == True:
            rotatedImg = cv.line(img, (topLeftPoint[0], topLeftPoint[1]), (topRightPoint[0], topRightPoint[1]), (0,0,255), 3)

            rotatedImg = cv.line(rotatedImg, (topLeftPoint[0], topLeftPoint[1]), (topLeftPoint[0], topLeftPoint[1]), (255,0,0), 15)

            rotatedImg = cv.line(rotatedImg, (topRightPoint[0], topRightPoint[1]), (topRightPoint[0], topRightPoint[1]), (0,255,0), 15)

        currentRotation = GetAngleOfLineBetweenTwoPoints( topLeftPoint[0], topLeftPoint[1], topRightPoint[0], topRightPoint[1] )


        minX = min(minX)
        minY = min(minY)
    
        maxX = max(maxX)
        maxY = max(maxY)   


        if console.popupDebug == True:
            cv.imshow('Before rotation', rotatedImg)
            cv.waitKey(0)

          
        console.PrintDebug('Angle to correct = ' + str( currentRotation ) )
        
        rotatedImg = rotatedImg[int(minY):int(maxY), int(minX):int(maxX)] 

        rotatedImg = ndimage.rotate(rotatedImg, currentRotation)   
        
        if console.popupDebug == True:
            cv.imshow('rotated', rotatedImg)
            cv.waitKey(0)


        decoded = decode( rotatedImg )
        if console.debug == True:
            print(decoded)

        if barcodeFound == False:

            if len(decoded)>0:
                barcodeFound = True

                barcode = 0

                
                console.PrintStatement('Barcode Found')

                # Print results
                for obj in decoded:
                    console.Print('Type : ' + str(obj.type) )
                    barcodeString = str(obj.data)
                    barcode = Search_number_String(barcodeString)
                    console.Print('Data : ' + barcode)


                if console.popupDebug == True:
                    console.PrintDebug(decoded)
                    cv.imshow('rotated', rotatedImg)
                    cv.waitKey(0)



        

                labelWidth = maxX - minX

                if console.popupDebug == True:
                    cv.imshow('cropped', rotatedImg)
                    cv.waitKey(0)

                console.Print('Label Width: ' + str(maxX) + 'px' )
                cv.imwrite(outputName_Path , rotatedImg )
                
            else:
                console.Print('Still Searching For Barcode')

    console.ClearLine()

    
    if barcodeFound == False:
        return 0, 0, "None"
    else:
        return barcode, labelWidth, outputName_Path







import numpy as np
import json
import os
from datetime import datetime
from math import pi
import conversions as convFunctions


def convertNpy(file,sourceType,targetType,outputFolder,hasTimeInfo):
    """
    The conversion function to be applies in all points of a file in order to produce
    a JSON output of transformed points.
    
    Args:
        file (file): The NPY file containing all points to be converted
        
        sourceType: The type of the information of each point: DEGREES(1), RADIANS(2) or REFERENCES(3)
        
        targetType: The type of the target information of each point: DEGREES(1), RADIANS(2) or REFERENCES(3)
        
        outputFolder: The folder where the translated content will be saved
        
        hasTimeInfo: A flag to inform if the file contains time information as las coordinate of each point
 
    Returns:
        string: The name of the saved file
    """
    
    arr = np.load(file)
    list = arr.tolist()
    #apply the conversion between sourceTye and targetType. they can assume values 1 (DEGREE),2(RADIANS),3 (REFS) and 4 (COUTNERS)
    convertedList = realConvert(list,sourceType,targetType,hasTimeInfo)
    json_str = json.dumps(convertedList)
    nameParts = file.split("/")
    name = nameParts[len(nameParts) - 1].split(".")
    now = datetime.now()
    convertedFileName = os.path.join(outputFolder, name[0] + "-" + now.strftime("%m-%d-%Y_%H:%M:%S") + ".json")
    with open(convertedFileName, "w") as outfile:
        outfile.write(json_str)
        
    print('converted file ', convertedFileName)
    return convertedFileName

def realConvert(list,sourceType,targetType,hasTimeInfo):
    #apply the conversion to each element (point) of the list and returns it
    convertedList = []
    for p in list:
        convertedList.append(convertPoint(p,sourceType,targetType,hasTimeInfo))
        
    return convertedList

def convertPoint(point, sourceType,targetType,hasTimeInfo):
    return lowLevelConvertion(point,sourceType,targetType,hasTimeInfo)

def lowLevelConvertion(point,sourceType,targetType,hasTimeInfo):
    """
        
    """
    convertedPoint = []
    conversionFunction = lambda x:0
    if sourceType == 1: #angle in degree
        if targetType == 2: #to radians
            conversionFunction = lambda x: pi*x/180.0
            if hasTimeInfo: # last coordinate is time and does not aplies to it
                for motor,coord in enumerate(point,start=1) :
                    if(motor < len(point)):
                        convertedPoint.append(conversionFunction(coord))
                    else:
                        convertedPoint.append(coord)
            else:
                for coord in point:
                    convertedPoint.append(conversionFunction(coord))
            
        elif targetType == 3: # to ref
            conversionFunction = convFunctions.angle_to_ref
            if hasTimeInfo: # last coordinate is time and does not aplies to it
                for motor,coord in enumerate(point,start=1) :
                    if(motor < len(point)):
                        convertedPoint.append(conversionFunction(motor,coord))
                    else:
                        convertedPoint.append(coord)
            else:
                for motor,coord in enumerate(point,start=1):
                    convertedPoint.append(conversionFunction(motor,coord))
                
    elif sourceType == 2: #angles in radians
        if targetType == 1: # to degree
            conversionFunction = lambda x: 180.0*x/pi
            if hasTimeInfo: # last coordinate is time and does not aplies to it
                for motor,coord in enumerate(point,start=1) :
                    if(motor < len(point)):
                        convertedPoint.append(conversionFunction(coord))
                    else:
                        convertedPoint.append(coord)
            else:
                for coord in point:
                    convertedPoint.append(conversionFunction(coord))
        elif targetType == 3: # to ref (radians to ref)
            # first converto from radians to degree and then from degree to ref
            intermediatePoint = lowLevelConvertion(point,2,1,hasTimeInfo)
            convertedPoint = lowLevelConvertion(intermediatePoint,1,3,hasTimeInfo)
    elif sourceType == 3: #refs
        if targetType == 1: #angles in degree
            conversionFunction = convFunctions.ref_to_angle
            if hasTimeInfo: # last coordinate is time and does not aplies to it
                for motor,coord in enumerate(point,start=1) :
                    if(motor < len(point)):
                        convertedPoint.append(conversionFunction(motor,coord))
                    else:
                        convertedPoint.append(coord)
            else:
                for motor,coord in enumerate(point,start=1):
                    convertedPoint.append(conversionFunction(motor,coord))
        elif targetType == 2: #angles in radians
            intermediatePoint = lowLevelConvertion(point,3,1,hasTimeInfo)
            convertedPoint = lowLevelConvertion(intermediatePoint,1,2,hasTimeInfo)

    return convertedPoint
import numpy as np
import json
import os

ident = 2

def convertNpy(file,sourceType,targetType,outputFolder):
    arr = np.load(file)
    list = arr.tolist()
    #apply the conversion between sourceTye and targetType. they can assume values 1 (DEGREE),2(RADIANS),3 (REFS) and 4 (COUTNERS)
    convertedList = realConvert(list,sourceType,targetType)
    json_str = json.dumps(convertedList)
    nameParts = file.split("/")
    name = nameParts[len(nameParts) - 1].split(".")
    convertedFileName = os.path.join(outputFolder, name[0] + ".json")
    with open(convertedFileName, "w") as outfile:
        outfile.write(json_str)
    
    return convertedFileName

def realConvert(list,sourceType,targetType):
    #apply the conversion to each element (point) of the list and returns it
    convertedList = []
    for p in list:
        convertedList.append(convertPoint(p,sourceType,targetType))
        
    return convertedList

def convertPoint(point, sourceType,targetType):
    return lowLevelConvertion(point,sourceType,targetType)

def lowLevelConvertion(point,sourceType,targetType):
    return [0,0,0]
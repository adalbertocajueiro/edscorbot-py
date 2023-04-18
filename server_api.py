import json
from datetime import datetime
from math import pi
import conversions as convFunctions

"""
    This map keeps specific functions to any robots to provide conversion support. 
    Robots are identified by a name and must have two conversion function implementations:
    `angle_to_ref` and `ref_to_angle` to be applied to each point of the trajectory.
    These funcions must be implemented in file conversions.py and added to this map
    as a new entry (key,value) in a similar way to the existing one.

    Returns:
        map<string,ojb>: a map containing the conversion functions for each robotic arm supported
        by this service
"""
robotFunctionsMap = {    
    'EDScorbot': {
        'angle_to_ref':  convFunctions.angle_to_ref_edscorbot,
        'ref_to_angle':  convFunctions.ref_to_angle_edscorbot  
    }
}

def convertNpy(listStr,sourceType,targetType,hasTimeInfo, robotName):
    """
    The conversion function to be applies in all points of a file in order to produce
    a JSON output of transformed points.
    
    Args:
        listStr: The content of a previously loaded NPY file as a list of points as string
        
        sourceType: The type of the information of each point: DEGREES(1), RADIANS(2) or REFERENCES(3)
        
        targetType: The type of the target information of each point: DEGREES(1), RADIANS(2) or REFERENCES(3)
        
        hasTimeInfo: A flag to inform if the file contains time information as las coordinate of each point
        
        robotName: The name of the robot to use the conversions
 
    Returns:
        convertedList: A list of points converted
    """
    list = json.loads(listStr)
    convertedList = []
    for p in list:
        convertedList.append(pointConversion(p,sourceType,targetType,hasTimeInfo,robotName))
        
    return convertedList

def realConvert(list,sourceType,targetType,hasTimeInfo,robotName):
    #apply the conversion to each element (point) of the list and returns it
    convertedList = []
    for p in list:
        convertedList.append(pointConversion(p,sourceType,targetType,hasTimeInfo,robotName))
        
    return convertedList

def pointConversion(point,sourceType,targetType,hasTimeInfo,robotName):
    """
    The low level function that converts one point (array/list of coordinates) into
    a point with coordinates in another (target) type. The function first captures
    the suitable conversion functions for the robotic arm (from the map) and uses
    them during the conversion. Each robot has its conversion functions that are maintained 
    in a map.
    
        Args:
            point: The point to be converted
            
            sourceType: The type of the information of each point: DEGREES(1), RADIANS(2) or REFERENCES(3)
            
            targetType: The type of the target information of each point: DEGREES(1), RADIANS(2) or REFERENCES(3)

            hasTimeInfo: A flag to inform if the file contains time information as las coordinate of each point
            
            robotName: The name of the robot
    
        Returns:
            point: A list of coordinates converted to the target type
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
            # gets the suitable function
            conversionFunction = robotFunctionsMap[robotName]["angle_to_ref"]
            #angles must be in radians
            intermediatePoint = pointConversion(point,1,2,hasTimeInfo,robotName)
            if hasTimeInfo: # last coordinate is time and does not aplies to it
                for motor,coord in enumerate(intermediatePoint,start=1) :
                    if(motor < len(intermediatePoint)):
                        convertedPoint.append(conversionFunction(motor,coord))
                    else:
                        convertedPoint.append(coord)
            else:
                for motor,coord in enumerate(intermediatePoint,start=1):
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
            # gets the suitable function
            conversionFunction = robotFunctionsMap[robotName]["angle_to_ref"]
            if hasTimeInfo: # last coordinate is time and does not aplies to it
                for motor,coord in enumerate(point,start=1) :
                    if(motor < len(point)):
                        convertedPoint.append(conversionFunction(motor,coord))
                    else:
                        convertedPoint.append(coord)
            else:
                for motor,coord in enumerate(point,start=1):
                    convertedPoint.append(conversionFunction(motor,coord))

    elif sourceType == 3: #refs
        if targetType == 1: #angles in degree
            # converts to an intermediate point in radians
            intermediatePoint = pointConversion(point,3,2,hasTimeInfo,robotName)
            #converts the intermediate point in radians to degree
            convertedPoint = pointConversion(intermediatePoint,2,1,hasTimeInfo,robotName)
        elif targetType == 2: #angles in radians
            conversionFunction = robotFunctionsMap[robotName]["ref_to_angle"]
            if hasTimeInfo: # last coordinate is time and does not aplies to it
                for motor,coord in enumerate(point,start=1) :
                    if(motor < len(point)):
                        convertedPoint.append(conversionFunction(motor,coord))
                    else:
                        convertedPoint.append(coord)
            else:
                for motor,coord in enumerate(point,start=1):
                    convertedPoint.append(conversionFunction(motor,coord))

    return convertedPoint
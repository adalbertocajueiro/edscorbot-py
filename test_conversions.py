import server_api as api
from math import pi

robotName = 'EDScorbot'
sourceType = 1
targetType = 2
points = [
    [0,0,0,0,0,0,200],
    [180,180,180,180,180,180,200]
]
hasTimeInfo = True

convertedList = api.realConvert(points,sourceType,targetType,hasTimeInfo,robotName)
print(' ')
print('TEST 1 - Conversion from DEGREE to RADIAN')
print('Original list: ', points)
print('Converted list: ', convertedList)

targetType = 3
convertedList = api.realConvert(points,sourceType,targetType,hasTimeInfo,robotName)
print(' ')
print('TEST 2 - Conversion from DEGREE to REFS')
print('Original list: ', points)
print('Converted list: ', convertedList)

points = [
    [0,0,0,0,0,0,200],
    [pi,pi,pi,pi,pi,pi,200]
]
sourceType = 2
targetType = 1
convertedList = api.realConvert(points,sourceType,targetType,hasTimeInfo,robotName)
print(' ')
print('TEST 3 - Conversion from RADIANS to DEGREE')
print('Original list: ', points)
print('Converted list: ', convertedList)

targetType = 3
convertedList = api.realConvert(points,sourceType,targetType,hasTimeInfo,robotName)
print(' ')
print('TEST 4 - Conversion from RADIANS to REFS')
print('Original list: ', points)
print('Converted list: ', convertedList)
'''
    This module work as a fake lib that provides the functions used by the routes 
    in the web api. The body of each function sould be adjusted to reuse the 
    functions of pyAER library suitably.
    Some high level requirements must be taken into account in this implementation:
    * each interaction with the robot requires a previous login to allow only authorized users
      connect to the arm
    * only ne user can use the arm at a time. 
    * the arm has to basic states: 'used' and 'free'. At startup, the arm is 'free'. 
      When a user connects to the arm (the connect method is successfully executed to a 
      specific user), it changes the state fo 'used'. Only when the disconnect method is 
      invoked (by the same user), the arm becomes 'free again'.
    * the pre-conditions for executing searchHome and move are
      - the state of the arm is 'used'
      - the invoker (user) is the same that holds the arm
    * probably the user (or his token) must be present as a data in the headers
    * all methods must be atomic, that is, only one of them must be executed at a time
    * for the sake of a better design, this module can be encapsulated into a singleton
'''

def npyToJson(sourceType, targetType,filePath):
    """
    It converts a EDScorbot NPY file in JSON format. The NPY file contains an array of arrays (N-dimensional)
    containing points (a tuple of coordinates). The value N depends of the number of joints of each arm.
    Depending on the target type, it applies transformation functions between the source and the target types.
    These functions are defined for each arm.

    :return: a JSON containing all points of the arm with a specific target type
    """
    return {'message':'Json generated'}

def npyToJsonPost(filePath,sourceType, targetType):
    """
    It converts a EDScorbot NPY file in JSON format. The NPY file contains an array of arrays (N-dimensional)
    containing points (a tuple of coordinates). The value N depends of the number of joints of each arm.
    Depending on the target type, it applies transformation functions between the source and the target types.
    These functions are defined for each arm.

    :return: a JSON containing all points of the arm with a specific target type
    """
    return {'message':'Json generated'}
  
def connect():
    ''' it calls the openUSB function in pyAER api/lib and returns the suitable result '''
    return {'message':'Connected to the server', 'status':'connected'}

def disconnect():
    return {'message':'Disconnected from server', 'status':'disconnected'}

def searchHome():
    ''' it calls the SearchHome function in pyAER api/lib and returns the suitable result'''
    return {'message':'Robot positioned at home', 'status':'arm moved'}

def move(trajectory):
    ''' it calls underlying functions in pyAER api/lib to move the arm according to all points in the trajectory and returns '''
    print('parameters'.format(trajectory))
    return {'message':'Trajectory applied to the robot', 'status':'arm moved'}
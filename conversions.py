
"""
    This modulueprovides conversions fuctions used by the front-end. 
    These functions are applicable individually to each motor to convert
    values between angles (degrees or radians) 
"""

from math import pi

"""
    This function converts angles to refs for each motor of the arm.
    Angles must be provided in degrees. Internally they are converted into radians. 
    The result is a ref value (int).
"""
def angle_to_ref(motor, angle):
    
    f = lambda x:0
    if motor == 1:
        f = lambda x:int(-3 * x)
    elif motor == 2:
        f = lambda x:int(-9.4 * x)
    elif motor == 3:
        f = lambda x:int(-3.1 * x)
    elif motor ==4:
        f = lambda x:int(-17.61158871 * x)
    
    degreesToRadians = lambda x: pi*x/180.0
    return f(degreesToRadians(angle))

"""
    This function converts refs to angles for each motor of the arm.
    Refs are integer values and angles are in degrees.
"""
def ref_to_angle(motor, ref):
    f = lambda x:0
    if motor == 1:
        f = lambda x:((-1 / 3) * x)
    elif motor == 2:
        f = lambda x:((-1 / 9.4) * x)
    elif motor == 3:
        f = lambda x:((-1 / 3.1) * x)
    elif motor ==4:
        f = lambda x:(-0.056780795 * x)
    
    radiansToDegrees = lambda x: 180.0*x/pi
    return radiansToDegrees(f(ref))

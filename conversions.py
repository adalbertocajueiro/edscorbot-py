
"""
    This modulueprovides conversions fuctions used by the front-end. 
    These functions are applicable individually to each motor to convert
    values between angles (degrees or radians) 
"""

from math import pi


def angle_to_ref_edscorbot(motor, angle):
    """
    This function converts angles to refs for each motor of the arm.
    It is assumed that the angle is given in radians. Internally they are converted into radians. 
    The result is a ref value (int).
    
        Args:
            motor: the motor to consider when applying the conversion
            
            angle: the angle in radians to be converted
    """
    
    f = lambda x:0  
    if motor == 1:  
        f = lambda x:int(-3 * x)    
    elif motor == 2:
        f = lambda x:int(-9.4 * x)
    elif motor == 3:
        f = lambda x:int(-3.1 * x)
    elif motor ==4:
        f = lambda x:int(-17.61158871 * x)
    
    return f(angle)


def ref_to_angle_edscorbot(motor, ref):
    """
    This function converts reference values to angles for each motor of the arm.
    References are integer values and angles are double values in radians.
    
        Args:
            motor: the motor to consider when applying the conversion
            
            ref: the reference value
    """

    f = lambda x:0
    if motor == 1:
        f = lambda x:((-1 / 3) * x)
    elif motor == 2:
        f = lambda x:((-1 / 9.4) * x)
    elif motor == 3:
        f = lambda x:((-1 / 3.1) * x)
    elif motor ==4:
        f = lambda x:(-0.056780795 * x)
    
    return f(ref)


def count_to_angle(motor, count):
    f = lambda x:0
    if motor == 1:
        f = lambda x:(1 / 125.5) * (x - 32768)
    elif motor == 2:
        f = lambda x:(1 / 131) * (x - 32768)
    elif motor == 3:
        f = lambda x:(1 / 127.7) * (count - 32768)
    elif motor ==4:
        f = lambda x:(0.012391573729863692) * (count - 32768)
    
    return f(count)

def ref_to_count(motor, ref):
    f = lambda x:0
    if motor == 1:
        f = lambda x:(40.35269645959781 * x) + 32768
    elif motor == 2:
        f = lambda x:(14.770677455806219 * x) + 32768
    elif motor == 3:
        f = lambda x:(41.6752813118148 * x) + 32768
    elif motor ==4:
        f = lambda x:(4.582209206643176 * x) + 32768
    
    return f(ref)

def count_to_ref(motor, count):
    f = lambda x:0
    if motor == 1:
        f = lambda x:(0.02478) * (x - 32768)
    elif motor == 2:
        f = lambda x:(0.0677) * (x - 32768)
    elif motor == 3:
        f = lambda x:(0.02399) * (x - 32768)
    elif motor ==4:
        f = lambda x:(0.2182353) * (x - 32768)
    
    return f(count)

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
    
    return f(angle)

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
    
    return f(ref)
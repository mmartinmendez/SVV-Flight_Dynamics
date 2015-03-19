from control.matlab import forced_response

def symetric_dynamic_response(sys,t,u):
    [T,y,x] = forced_response(sys,u,t)
    return T,y,x

def asymetric_dynamic_response(sys,t,u):
    [T,y,x] = forced_response(sys,u,t)
    return T,y,x
import control as cm

def dynamic_response(sys,t,u):
    [T,y,x] = cm.forced_response(sys,t,u)
    return T,y,x

import control as cm

def dynamic_response(sys,t0,u):
    [t,y,x] = lsim(sys,u,t0)
    return t,y,x

def dynamic_response1(sys,t0,u):
    [t,y,x] = cm.forced_response(sys,t,u)
    return t,y,x



from control.matlab import *

def dynamic_response(sys,t0,u):
    x0 = [[0],
          [0],
          [0],
          [0]]
    [y,t,x] = lsim(sys,u,t0,x0)
    print u
    print t
    return t,y,x

def dynamic_response1(sys,t0,u):
    [t,y,x] = cm.forced_response(sys,t0,u)
    return t,y,x


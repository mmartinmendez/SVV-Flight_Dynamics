
from control.matlab import *
from Cit_par import *
def dynamic_response(sys,t0,u):
    x0 = [[V0],
          [alpha0],
          [th0],
          [0.014]]
    y,t,x = lsim(sys,u,t0,x0)
    #y,t = impulse(sys,t0)
    #y,t = initial(sys, t0, x0)
    #x = 0
    #print t
    #print y
    #print x
    return t,y,x

def dynamic_response1(sys,t0,u):
    [t,y,x] = cm.forced_response(sys,t0,u)
    return t,y,x


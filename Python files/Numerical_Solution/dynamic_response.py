
from control.matlab import *
from Cit_par import*

def dynamic_response(sys,t0,u):
    x0 = [[0],
          [0],
          [0],
          [0]]
    [y,t,x] = lsim(sys,u,t0,x0)
    return t,y,x



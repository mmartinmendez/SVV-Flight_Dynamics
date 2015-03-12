<<<<<<< HEAD
# -*- coding: utf-8 -*-

from numpy import matrix
from Cit_par import*
import control

def stateSpaceSymmetric():
    C1=c/V0*matrix([[-2*muc,0,0,0],
               [0,{CZadot-2*muc},0,0],
               [0,0,-1,0],
               [0,Cmadot,0,-2*muc*KY2]])
    C2=matrix([[CXu,CXa,CZ0,CXq],
               [CZu,CZa,-CX0,CZq+2*muc],
               [0,0,0,1],
               [Cmu,Cma,0,Cmq]])
    C3=matrix([CXde],
              [CZde],
              [0],
              [Cmde])

    A=C1.I * C2
    B=C1.I * C3
    C=matrix([0,1,0,0])
    D=matrix([0])
    sys1 = ss(A,B,C,D)
    return sys1

def stateSpaceAsymmetric():
    C1=b/V0*matrix([[CYb-2mub,0,0,0],
                    [0,-1/2,0,0],
                    [0,0,-4*mub*KX2,4*mub*KXZ],
                    [Cnb,0,4*mub*KXZ,-4*mub*KZ2]])
    C2=matrix([[CYb,CL,CYp,CYr-4*mub],
               [0,0,1,0],
               [Clb,0,Clp,Clr],
               [Cnb,0,Cnp,Cnr]])
    C3=matrix([[CYda,CYdr],
               [0,0],
               [Clda,Cldr],
               [Cnda,Cndr]])

    A=C1.I * C2
    B=C1.I * C3
    C=matrix([0,1,0,0])
    D=matrix([0])
    sys2 = ss(A,B,C,D)
    return sys2
=======
#import lti What is this module called
def statespace(C_1,C_2,C_3,u):
    sys = 0 #calculate sys with lti module
    return sys
>>>>>>> origin/master

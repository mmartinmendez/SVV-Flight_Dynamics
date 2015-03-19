
#put in comments!
#==============+==============
from numpy import matrix
from Cit_par import*
from control.matlab import*



def stateSpaceSymmetric(val):
    C1=matrix([[-2*muc,0,0,0],
               [0,CZadot-2*muc,0,0],
               [0,0,-1.,0],
               [0,Cmadot,0,-2*muc*KY2]])
    C2=matrix([[CXu,CXa,CZ0,CXq],
               [CZu,CZa,-CX0,CZq+2*muc],
               [0,0,0,1.],
               [Cmu,Cma,0,Cmq]])
    C3=matrix([[CXde],
              [CZde],
              [0],
              [Cmde]])

    A=-C1.I * C2
    B=-C1.I * C3
    if val==1:
        C=matrix([1,0,0,0])
    elif val==2:
        C=matrix([0,1,0,0])
    elif val==3:
        C=matrix([0,0,1,0])
    elif val==4:
        C=matrix([0,0,0,1])
    D=matrix([0])
    sys1 = ss(A,B,C,D)
    return sys1


def stateSpaceAsymmetric(val):
    C1=matrix([[CYbdot-2*mub,0,0,0],
                    [0,-1/2.,0,0],
                    [0,0,-4*mub*KX2,4*mub*KXZ],
                    [Cnbdot,0,4*mub*KXZ,-4*mub*KZ2]])
    C2=matrix([[CYb,CL,CYp,CYr-4*mub],
               [0,0,1.,0],
               [Clb,0,Clp,Clr],
               [Cnb,0,Cnp,Cnr]])
    C3=matrix([[CYda,CYdr],
               [0,0],
               [Clda,Cldr],
               [Cnda,Cndr]])

    A=-C1.I * C2
    B=-C1.I * C3
    if val==1:
        C=matrix([1,0,0,0])
    elif val==2:
        C=matrix([0,1,0,0])
    elif val==3:
        C=matrix([0,0,1,0])
    elif val==4:
        C=matrix([0,0,0,1])
    D=matrix([0,0])
    sys2 = ss(A,B,C,D)
    return sys2

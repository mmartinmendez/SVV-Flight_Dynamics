
#put in comments!
#==============+==============

from Cit_par import*
from control.matlab import*



def stateSpaceSymmetric():

    C1=c/V0*matrix([[(-2*muc)/V0,0,0,0],
               [0,CZadot-2*muc,0,0],
               [0,0,-1.,0],
               [0,Cmadot,0,(-2*muc*KY2)*c/V0]])
    C2=matrix([[-CXu/V0,-CXa,-CZ0,-CXq*c/V0],
               [-CZu/V0,-CZa,CX0,-(CZq+2*muc)*c/V0],
               [0,0,0,-c/V0],
               [-Cmu/V0,-Cma,0,-Cmq*c/V0]])
    C3=matrix([[-CXde],
              [-CZde],
              [0],
              [-Cmde]])

    A=C1.I * C2
    B=C1.I * C3
    C=eye(4)
    D=[[0],[0],[0],[0]]
    sys1 = ss(A,B,C,D)
    return sys1


def stateSpaceAsymmetric():
    C1=b/V0*matrix([[CYbdot-2*mub,0,0,0],
                    [0,-1/2.,0,0],
                    [0,0,-2*mub*KX2*b/V0,2*mub*KXZ*b/V0],
                    [Cnbdot,0,2*mub*KXZ*b/V0,-2*mub*KZ2*b/V0]])
    C2=matrix([[CYb,CL,CYp*b/(2*V0),CYr-2*mub*b/V0],
               [0,0,b/(2*V0),0],
               [Clb,0,Clp*b/(2*V0),Clr*b/(2*V0)],
               [Cnb,0,Cnp*b/(2*V0),Cnr*b/(2*V0)]])
    C3=matrix([[CYda,CYdr],
               [0,0],
               [Clda,Cldr],
               [Cnda,Cndr]])

    A=-C1.I * C2
    B=-C1.I * C3
    C=eye(4)
    D=[[0],[0],[0],[0]]
    sys2 = ss(A,B,C,D)
    return sys2

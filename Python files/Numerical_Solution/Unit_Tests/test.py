__author__ = 'myth'

from numpy import matrix,linalg
from data import*
from control.matlab import*

C1=b/V*matrix([[-2*mub,0,0,0],
           [0,-1/2.,0,0],
           [0,0,-4*mub*KX2,4*mub*KXZ],
           [0,0,4*mub*KXZ,-4*mub*KZ2]])

C2=matrix([[-CYb,-CL,-CYp,-(CYr-4*mub)],
           [0,0,-1,0],
           [-Clb,0,-Clp,-Clr],
           [-Cnb,0,-Cnp,-Cnr]])

C3=matrix([[-CYda,-CYdr],
           [0,0],
           [-Clda,-Cldr],
           [-Cnda,-Cndr]])

A=C1.I*C2
print C1
print C2
print C3
print linalg.eigvals(A)
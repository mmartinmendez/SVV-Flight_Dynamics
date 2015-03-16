__author__ = 'myth'

from numpy import*
from Cit_par import*

C1=matrix([[-2*muc,0,0,0],
               [0,CZadot-2*muc,0,0],
               [0,0,-1,0],
               [0,Cmadot,0,-2*muc*KY2]])
C2=matrix([[CXu,CXa,CZ0,CXq],
            [CZu,CZa,-CX0,CZq+2*muc],
            [0,0,0,1],
             [Cmu,Cma,0,Cmq]])
C3=matrix([[CXde],
            [CZde],
            [0],
            [Cmde]])

print C1
print C2
print C3
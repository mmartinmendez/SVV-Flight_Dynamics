__author__ = 'myth'

from numpy import*

from control.matlab import*

A = [[-0.313, 56.7, 0],[ -0.0139, -0.426, 0],[ 0, 56.7, 0]]
B = [[0.232],[ 0.0203],[ 0]]
C = [0, 0 ,1]
D = [0]
pitch_ss = ss(A,B,C,D)



t=np.linspace(0,20,100)

u=np.zeros(100)

lsim()
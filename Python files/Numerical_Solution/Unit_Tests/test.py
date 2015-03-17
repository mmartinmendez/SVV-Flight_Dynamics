__author__ = 'myth'

from numpy import matrix,linalg
from data import*
from math import*
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
eigenvalues = linalg.eigvals(A)

final = []
for i in range(len(eigenvalues)):
    result = []
    if eigenvalues[i].imag!=0:
        result.append(eigenvalues[i])
        result.append((2*pi)/eigenvalues[i].imag*c/V)
        result.append(log(0.5)/eigenvalues[i].real*c/V)
        result.append(eigenvalues[i].real/(sqrt((eigenvalues[i].real)**2+(eigenvalues[i].imag)**2)))
        result.append(sqrt((eigenvalues[i].real)**2+(eigenvalues[i].imag)**2))
    else:
        result.append(eigenvalues[i])
        result.append(0)
        result.append(log(0.5)/eigenvalues[i].real*c/V)
        result.append(0)
        result.append(0)
    final.append(result)
print final
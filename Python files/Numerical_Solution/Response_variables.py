from numpy import*
from math import*
from Cit_par import*

def Response_symmetric(eigenvalues):
    result = []
    if eigenvalues.imag!=0:
        result.append(eigenvalues)
        result.append((2*pi)/eigenvalues.imag*c/V0)
        result.append(log(0.5)/eigenvalues.real*c/V0)
        result.append(-eigenvalues.real/(sqrt((eigenvalues.real)**2+(eigenvalues.imag)**2)))
        result.append(sqrt((eigenvalues.real)**2+(eigenvalues.imag)**2)*V0/c)
    else:
        result.append(eigenvalues)
        result.append(0)
        result.append(log(0.5)/eigenvalues.real*c/V0)
        result.append(0)
        result.append(0)

    return result

def Response_Asymmetric(eigenvalues):
    result = []
    if eigenvalues.imag!=0:
        result.append(eigenvalues)
        result.append((2*pi)/eigenvalues.imag*b/V0)
        result.append(log(0.5)/eigenvalues.real*b/V0)
        result.append(-eigenvalues.real/(sqrt((eigenvalues.real)**2+(eigenvalues.imag)**2)))
        result.append(sqrt((eigenvalues.real)**2+(eigenvalues.imag)**2)*V0/b)
    else:
        result.append(eigenvalues)
        result.append(0)
        result.append(log(0.5)/eigenvalues.real*b/V0)
        result.append(0)
        result.append(0)

    return result
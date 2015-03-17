from numpy import*
from math import*
from Cit_par import*

def Response(eigenvalues):
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
    return final
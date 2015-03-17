from numpy import*
from math import*
from Cit_par import*

def Period(eigenvalues):
    result = zeros(len(eigenvalues))
    for i in range(len(eigenvalues)):
        if isinstance(eigenvalues[i],complex):
            result[i]=eigenvalues[i]
            result[i].append((2*pi)/eigenvalues[i].imag*c/V)
            result[i].append(log(1/2)/eigenvalues[i].real*c/V)
            result[i].append(eigenvalues[i].real/(sqrt((eigenvalues[i].real)**2+(eigenvalues[i].imag)**2)))
            result[i].append(sqrt((eigenvalues[i].real)**2+(eigenvalues[i].imag)**2))
        else:
            result[i]=eigenvalues[i]
            result[i].append(0)
            result[i].append(log(1/2)/eigenvalues[i].real*c/V)
            result[i].append(0)
            result[i].append(0)

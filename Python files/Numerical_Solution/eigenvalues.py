from control.matlab import*
from numpy import linalg

def eigenvalues(sys):
    [a,b,c,d] = ssdata(sys)
    eig = linalg.eigvals(a)
    return eig
'''
Calculates drag coefficient using D=T, thus assuming non-accalerating flight.
Input: Density, Wing Area, Tr
Output: Drag coefficient
Output format: array with same lenght as arrays V and T_p
'''
import numpy as np

def C_D(T_p,rho_0,V,S):
    T_p = [ sum(x) for x in zip(*np.transpose(T_p)) ]
    CD = T_p*(0.5*rho_0*np.square(V)*S)**-1
    return CD

#============test============
#T = np.arange(0.5,0,-0.1)
#V = np.ones(len(T))
#S = 10
#rho_0 = 1
#CD = C_D(T,rho_0,V,S)
#print CD    
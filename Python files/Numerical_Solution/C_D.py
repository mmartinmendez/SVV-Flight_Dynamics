'''
Calculates drag coefficient using D=T, thus assuming non-accalerating flight.
Input: Density, Wing Area, Tr
Output: Drag coefficient
Output format: array with same lenght as arrays V and T_p
'''
import numpy as np

def C_D(T_p,rho_0,V,S):
    CD = T_p*(0.5*rho_0*np.square(V)*S)**-1
    return CD
'''
Calculates drag coefficient using D=T, thus assuming non-accalerating flight.
Input: Density, Wing Area, Tr
Output: Drag coefficient
Output format: float
'''

def C_D(rho,S,V,T_p):
    CD = T_p/(0.5*rho*V**2*S)
    return CD
import numpy as np

def C_L(W,rho_0,V,S):
    CL = W*(0.5*rho_0*np.square(V)*S)**-1
    return CL

#============test============
#W = np.arange(5,0,-1)
#V = 3*np.ones(len(W))
#S = 10
#rho_0 = 1
#CL = C_L(W,rho_0,V,S)
#print CL
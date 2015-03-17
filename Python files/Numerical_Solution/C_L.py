import numpy as np

def C_L(W,rho_0,V,S):
    CL = W*(0.5*rho_0*np.square(V*0.514444444)*S)**-1
    return CL

#============test============
#W = np.arange(5,0,-1)
#V = np.ones(len(W))
#S = 10
#rho_0 = 1
#CL = C_L(W,V,S,rho_0)
#print CL
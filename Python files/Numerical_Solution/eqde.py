import numpy as np
import math as m

def eqde(de,Cmde,T,CmTc,Ve,S):
    T = [ sum(x) for x in zip(*np.transpose(T)) ]
    T = np.array(T)
    eqde = de*m.pi/180-CmTc*(T[1::2]-T[::2])*(0.5*1.225*Ve**2*S*Cmde)**-1
    return eqde # [rad]
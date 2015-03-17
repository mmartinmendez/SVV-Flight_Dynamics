import matplotlib.pyplot as plt
import numpy as np

def C_L2vsC_Dplot(C_L,C_D,value = None):
    if len(C_L) != len(C_D):
        raise IOError("arrays C_L and C_D not of equal lenght")
    C_L2 = np.square(C_L)
    CD2_ployfit = np.polyfit(C_L2,C_D,1)
    CD2_ployfit = np.poly1d(CD2_ployfit)
    x = np.linspace(C_L2[0]-1,C_L2[-1],100)
    plt.figure()
    plt.plot(C_D,C_L2,'.',CD2_ployfit(x),x,'-')
    plt.show()
    if value == None:
        return CD2_ployfit
    else:
        return CD2_ployfit(value)

#==========test==========#
#from random import randint
#import math as m
#C_L = np.arange(0,5,0.1)
#C_D_0 = np.ones(len(C_L))*0.5
#A = 5
#e = 1
#C_D = C_D_0 + C_L**2/(m.pi*A*e)
#for i in range(len(C_D)):
#    C_D[i] += randint(-1,1)*0.1
#print(C_LvsC_Dplot(C_L,C_D,value = 0))
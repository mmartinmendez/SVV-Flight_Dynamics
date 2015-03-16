'''
Calculates Drag for an arbitrary C_L, based on a quadratic fit of C_L vs. C_D
Input: Lift coefficient and Drag coefficient (both arrays of equal length)
Output: if value=None (default): function of Drag coefficient in terms of Lift Coefficient 
        else: Drag coefficient for a perticular Lift coefficient
Output format:  if value=None (default):function(array) 
                else: float
'''

import matplotlib.pyplot as plt
import numpy as np

def C_LvsC_Dplot(C_L,C_D,value = None):
    if len(C_L) != len(C_D):
        raise IOError("arrays C_L and C_D not of equal lenght")
    CD_polyfit = np.polyfit(C_L,C_D,2)
    CD_polyfit = np.poly1d(CD_polyfit)
    x = np.linspace(C_L[0]-1,C_L[-1],100)
    plt.plot(C_D,C_L,'.',CD_polyfit(x),x,'-')
    plt.show()
    if value == None:
        return CD_polyfit
    else:
        return CD_polyfit(value)

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
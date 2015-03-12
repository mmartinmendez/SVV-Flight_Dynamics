'''
Input: polyfit of C_L vs C_D
'''

def C_D_0(CD_polyfit):
    return CD_polyfit(0)

#==========test==========#
#from random import randint
#import numpy as np
#import math as m
#from C_LvsC_Dplot import C_LvsC_Dplot
#C_L = np.arange(0,5,0.1)
#C_d_0 = np.ones(len(C_L))*0.5
#A = 5
#e = 1
#C_D = C_d_0 + C_L**2/(m.pi*A*e)
#for i in range(len(C_D)):
#    C_D[i] += randint(-1,1)*0.1
#CD_polyfit = C_LvsC_Dplot(C_L,C_D)
#print(C_D_0(CD_polyfit))
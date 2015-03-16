__author__ = 'myth'

#clear the terminal
import os
clear = lambda: os.system('cls')
clear()
#close all plots
import matplotlib.pyplot as plt
plt.close("all")

import ISA, C_L, C_D, C_L_alpha, C_D_alpha, input, weight, oswaldfactor
from Cit_par import*
from state_space import*
from numpy import*

class Main:
    def __init__(self,h,p,S,V,T_p,W_S,filename1,filename2):                 #Initializes all the varibles needed
        print 'initializing............'
        self.h1=h
        self.p=p
        self.S=S
        self.V=V
        self.T_p=T_p
        self.W_S=W_S
        self.filename1=filename1
        self.filename2=filename2
        self.data,self.weights=input.inputFile(self.filename1,self.filename2)
        #names for arrays of files: statCLCD, statDEV (for elevator-trim) and statCG (for cg_shift)
    def firstMeasurementSeries(self):   # Call all functions needed for calculation in the first measurement series
        print 'First Measurement Series Calculation: Begin'
        a,b,c = ISA.aparameters(self.h1)
        W = weight.weight(self.W_S,self.weights,self.statCLCD[8],g)
        CL = C_L(W,rho0,self.statCLCD[4],S)
        T_p = 1200*np.ones(6)#Temporary value
        CD = C_D(T_p,rho0,self.statCLCD[4],S)
        CD_polyfit = C_LvsC_Dplot(CL,CD)
        CD0 = C_D_0(CD_polyfit)
        print 'CD0 = ' + str(CD0)
        CD2_polyfit = C_L2vsC_Dplot(CL,CD)
        e = oswaldfactor(CD2_polyfit,A)
        print 'e = ' + str(e)
        CLa_polyfit = CL_alpha(self.statCLCD[5],CL)
        CDa_polyfit = CD_alpha(self.statCLCD[5],CD)
        print 'First Measurement Series Calculation: End'

    def secondMeasurementSeries(self):              # Call all functions needed for calculation in the second measurement series
        print 'Second Measurement Series Calculation: Begin'
        delta_evsVplot(self.statDEV[6],self.statDEV[4])
        print 'Second Measurement Series Calculation: End'

    def dynamicMeasurementSeries(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Dynamic Measurement Series Calculation: Begin'
        W = weight.weight(self.W_S,self.weights,self.data[5:7],g)
        stateSpaceSymmetric()
        print 'Dynamic Measurement Series Calculation: End'

def init():
    """

    :rtype : object
    """
    h=0
    p=12000.
    S=15
    V=100
    T_p=1200
    filename1 = 'FTISxprt-20150305_144557.txt'
    filename2 = 'weights.txt'
    W_S = 60500 #[N]
    ap = Main(h,p,S,V,T_p,W_S,filename1,filename2)
    return ap

if __name__== "__main__":
    ap = init()
    ap.firstMeasurementSeries()
    ap.secondMeasurementSeries()
    ap.dynamicMeasurementSeries()


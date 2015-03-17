__author__ = 'myth'

#clear the terminal
import os
clear = lambda: os.system('cls')
clear()
#close all plots
import matplotlib.pyplot as plt
plt.close("all")


import ISA, C_L, C_D, C_L_alpha, C_D_alpha, input, weight, oswaldfactor, Veq, eigenvalues, Response_variables, C_LvsC_Dplot, C_L2vsC_Dplot, delta_evsVplot
from Cit_par import*
from state_space import*
from numpy import*

class Main:
    def __init__(self,h,p,S,V,T_p,W_S,filename1,filename2,filename3,filename4,filename5,filename6):                 #Initializes all the varibles needed
        print 'initializing............'
        self.h1=h
        self.p=p
        self.S=S
        self.V=V
        self.T_p=T_p
        self.W_S=W_S
        self.filename1=filename1
        self.filename2=filename2
        self.filename3=filename3
        self.filename4=filename4
        self.filename5=filename5
        self.filename6=filename6
        self.data,self.weights,self.statCG,self.statCLCD,self.statDEV,self.thrust=input.inputFile(self.filename1,self.filename2,self.filename3,self.filename4,self.filename5,self.filename6)
        #names for arrays of files: statCLCD, statDEV (for elevator-trim) and statCG (for cg_shift)

    def firstMeasurementSeries(self):   # Call all functions needed for calculation in the first measurement series
        print 'First Measurement Series Calculation: Begin'
#        a,b,c = ISA.aparameters(self.h1)
        W = weight.weight(self.W_S,self.weights,self.statCLCD[:,-2],g)
        CL = C_L.C_L(W,rho0,self.statCLCD[:,3],S)
        CD = C_D.C_D(self.thrust[:6,0],rho0,self.statCLCD[:,3],S)
        CD_polyfit = C_LvsC_Dplot.C_LvsC_Dplot(CL,CD)
        CD0 = C_D_0.C_D_0(CD_polyfit)
        print 'CD0 = ' + str(CD0)
        CD2_polyfit = C_L2vsC_Dplot.C_L2vsC_Dplot(CL,CD)
        e = oswaldfactor.oswaldfactor(CD2_polyfit,A)
        print 'e = ' + str(e)
        CLa_polyfit = C_L_alpha.CL_alpha(self.statCLCD[:,4],CL)
        CDa_polyfit = C_D_alpha.CD_alpha(self.statCLCD[:,4],CD)
        print 'CLalpha = ' + str(CLa_polyfit[1])
        print 'CDalpha = '
        print CDa_polyfit
        print 'First Measurement Series Calculation: End'

    def secondMeasurementSeries(self):              # Call all functions needed for calculation in the second measurement series
        print 'Second Measurement Series Calculation: Begin'
        print self.statDEV
        W = weight.weight(self.W_S,self.weights,self.statDEV[:,10],g)
        Ve = Veq.Veq(self.statDEV[:,3],W,self.W_S)
        delta_evsVplot.delta_evsVplot(self.statDEV[:,5],Ve)
        
        print 'Second Measurement Series Calculation: End'

    def dynamicMeasurementSeries(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Dynamic Measurement Series Calculation: Begin'
        #W = weight.weight(self.W_S,self.weights,self.data[5:7],g)
        sys1 = stateSpaceSymmetric()
        eig_symmetric = array(eigenvalues.eigenvalues(sys1))
        sys2 = stateSpaceAsymmetric()
        eig_asymmetric = array(eigenvalues.eigenvalues(sys2))
        eigen = append(eig_symmetric,eig_asymmetric)
        eigen.tolist()

        result = Response_variables.Response(eigen)

     #   short_period()
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
    filename3 = 'stationary_cg_shift.txt'
    filename4 = 'stationary_CL-CD.txt'
    filename5 = 'stationary_elevator-trim.txt'
    filename6 = 'stationarythrust.txt'
    W_S = 60500 #[N]
    ap = Main(h,p,S,V,T_p,W_S,filename1,filename2,filename3,filename4,filename5,filename6)
    return ap

if __name__== "__main__":
    ap = init()
    ap.firstMeasurementSeries()
    #ap.secondMeasurementSeries()
    ap.dynamicMeasurementSeries()


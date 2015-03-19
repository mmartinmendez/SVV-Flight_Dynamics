__author__ = 'myth'

#clear the terminal
import os
clear = lambda: os.system('cls')
clear()
#close all plots
import matplotlib.pyplot as plt
plt.close("all")


import ISA, C_L, C_D,C_D_0, C_L_alpha,C_m_alpha,eqde,eqfe,FevsVplot,C_m_delta, C_D_alpha, input, weight,x_cg , oswaldfactor, Veq, C_LvsC_Dplot, C_L2vsC_Dplot, delta_evsVplot, eigenvalues, Response_variables,Tp
from Cit_par import*
from state_space import*
from numpy import*
from math import *

class Main:
    def __init__(self,T_p,W_S,filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8):                 #Initializes all the varibles needed
        print 'initializing............'
        self.T_p=T_p
        self.W_S=W_S
        self.data,self.weights,self.statCG,self.statCLCD,self.statDEV,self.thrust,self.moment,self.arm=input.inputFile(filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8)
        #names for arrays of files: statCLCD, statDEV (for elevator-trim) and statCG (for cg_shift)

    def firstMeasurementSeries(self):   # Call all functions needed for calculation in the first measurement series
        print 'First Measurement Series Calculation: Begin'

#        a,b,c = ISA.aparameters(self.h1)
#===============old=============
#        W = weight.weight1(self.W_S,self.weights,self.statCLCD[:,-2],g)
#        CL = C_L.C_L(W,rho0,self.statCLCD[:,3]/1.94384449,S)
#        CD = C_D.C_D(self.thrust[0:12:2,:],rho0,self.statCLCD[:,3]/1.94384449,S)
#===============new=============        
        W = weight.weight1(self.W_S,self.weights,self.statCLCD[:,-2],g)
        Ve = Veq.Veq(self.statCLCD[:,3],W,self.W_S)
        CL = C_L.C_L(np.ones(len(Ve))*self.W_S,rho0,Ve,S)
        CD = C_D.C_D(self.thrust[0:12:2,:],rho0,Ve,S)
        CD_polyfit = C_LvsC_Dplot.C_LvsC_Dplot(CL,CD)
        CD2_polyfit = C_L2vsC_Dplot.C_L2vsC_Dplot(CL,CD)
        CD0 = C_D_0.C_D_0(CD2_polyfit)
        print 'CD0 = ' + str(CD0)
        e = oswaldfactor.oswaldfactor(CD2_polyfit,A)
        print 'e = ' + str(e)
        CLa_polyfit = C_L_alpha.CL_alpha(self.statCLCD[:,4],CL)
        CDa_polyfit = C_D_alpha.CD_alpha(self.statCLCD[:,4],CD)
        print 'CLalpha = ' + str(CLa_polyfit[1]*180/pi)
        print 'First Measurement Series Calculation: End'

    def secondMeasurementSeries(self):              # Call all functions needed for calculation in the second measurement series
        print 'Second Measurement Series Calculation: Begin'
        #print self.statDEV
        WCG = weight.weight1(self.W_S,self.weights,self.statCG[:,-2],g)
        VeCG = Veq.Veq(self.statCG[:,3],WCG,self.W_S)
        CL = C_L.C_L(np.ones(len(VeCG))*self.W_S,rho0,VeCG,S)
        dxcg = x_cg.x_cg(self.W_S,self.weights,self.statCG[:,-2],self.moment,self.arm,WCG,g)
        dde = (self.statCG[0,5]-self.statCG[1,5])*pi/180
        Cmdelta = C_m_delta.C_m_delta((CL[0]+CL[1])/2,dxcg,dde,c)
        print 'C_m_delta_e = ' + str(Cmdelta)
        W = weight.weight1(self.W_S,self.weights,self.statDEV[:,-2],g)
        Ve = Veq.Veq(self.statDEV[:,3],W,self.W_S)
        eqdelta = eqde.eqde(self.statDEV[:,5],Cmdelta,self.thrust[12:-4,:],CmTc,Ve,S)
        deltae_polyfit = delta_evsVplot.delta_evsVplot(eqdelta,Ve)
        eqFe = eqfe.eqfe(self.statDEV[:,7],self.W_S,W)
        Fe_polyfit = FevsVplot.FevsVplot(eqFe,Ve)
        Cma = C_m_alpha.C_m_alpha(self.statDEV[:,4],eqdelta,Cmdelta)
        print 'C_m_alpha = ' + str(Cma)
        print 'Second Measurement Series Calculation: End'


    def shortPeriod(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Short Period Calculation: Begin'
        W = weight.weight(self.W_S,self.weights,self.data[2:],g)
        open('input.txt', 'w').close()
        file = open('input.txt','w')
        file.write(str(self.data[29949][17]))
        file.write('\n')
        file.write(str(self.data[29949][19]))
        file.write('\n')
        file.write(str(self.data[29949][0]))
        file.write('\n')
        file.write(str(self.data[29949][12]))
        file.write('\n')
        file.write(str((W[30191])/g))
        file.close()

        execfile('Cit_par.py')

        sys1 = stateSpaceSymmetric()
        eig_symmetric = array(eigenvalues.eigenvalues(sys1))
        result = Response_variables.Response(eig_symmetric)
        print m,hp0,V0,rho,muc,mub
        print result
        print 'Short Period Calculation: End'

    def phugoid(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Phugoid Calculation: Begin'
        W = weight.weight(self.W_S,self.weights,self.data[2:],g)
        open('input.txt', 'w').close()
        file = open('input.txt','w')
        file.write(str(self.data[30630][17]))
        file.write('\n')
        file.write(str(self.data[30630][19]))
        file.write('\n')
        file.write(str(self.data[30630][0]))
        file.write('\n')
        file.write(str(self.data[30630][12]))
        file.write('\n')
        file.write(str(W[31636]))
        file.close()

        execfile('Cit_par.py')

        sys1 = stateSpaceSymmetric()
        eig_symmetric = array(eigenvalues.eigenvalues(sys1))
        eig_symmetric.tolist()
        result = Response_variables.Response(eig_symmetric)
        print m,hp0,V0,rho
        print result[1]
        print 'Phugoid Calculation: End'

    def aperiodicRoll(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Aperiodic Roll Calculation: Begin'
        W = weight.weight(self.W_S,self.weights,self.data[2:],g)
        open('input.txt', 'w').close()
        file = open('input.txt','w')
        file.write(str(self.data[29100][17]))
        file.write('\n')
        file.write(str(self.data[29100][19]))
        file.write('\n')
        file.write(str(self.data[29100][0]))
        file.write('\n')
        file.write(str(self.data[29100][12]))
        file.write('\n')
        file.write(str(W[29312]))
        file.close()

        sys1 = stateSpaceAsymmetric()
        eig_asymmetric = array(eigenvalues.eigenvalues(sys1))
        eig_asymmetric.tolist()
        result = Response_variables.Response(eig_asymmetric)
        print m,hp0,V0,rho
        print result[1]
        print 'Aperiodic Roll Calculation: End'

    def dutchRoll(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Dutch Roll Calculation: Begin'
        W = weight.weight(self.W_S,self.weights,self.data[2:],g)
        open('input.txt', 'w').close()
        file = open('input.txt','w')
        file.write(str(self.data[33000][17]))
        file.write('\n')
        file.write(str(self.data[33000][19]))
        file.write('\n')
        file.write(str(self.data[33000][0]))
        file.write('\n')
        file.write(str(self.data[33000][12]))
        file.write('\n')
        file.write(str(W[33313]))
        file.close()

        sys1 = stateSpaceAsymmetric()
        eig_asymmetric = array(eigenvalues.eigenvalues(sys1))
        eig_asymmetric.tolist()
        result = Response_variables.Response(eig_asymmetric)
        print m,hp0,V0,rho
        print result[1]
        print 'Dutch Roll Calculation: End'

    def aperiodicSpiral(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Aperiodic Spiral Calculation: Begin'
        W = weight.weight(self.W_S,self.weights,self.data[2:],g)
        open('input.txt', 'w').close()
        file = open('input.txt','w')
        file.write(str(self.data[35580][17]))
        file.write('\n')
        file.write(str(self.data[35580][19]))
        file.write('\n')
        file.write(str(self.data[35580][0]))
        file.write('\n')
        file.write(str(self.data[35580][12]))
        file.write('\n')
        file.write(str(W[37100]))
        file.close()

        sys1 = stateSpaceAsymmetric()
        eig_asymmetric = array(eigenvalues.eigenvalues(sys1))
        eig_asymmetric.tolist()
        result = Response_variables.Response(eig_asymmetric)
        print m,hp0,V0,rho
        print result[1]
        print 'Aperiodic Spiral Calculation: End'


def init():
    """

    :rtype : object
    """
    T_p=1200.
    filename1 = 'FTISxprt-20150305_144557.txt'
    filename2 = 'weights.txt'
    filename3 = 'stationary_cg_shift.txt'
    filename4 = 'stationary_CL-CD.txt'
    filename5 = 'stationary_elevator-trim.txt'
    filename6 = 'statthrust.dat'
    filename7 = 'fuel_moments.txt'
    filename8 = 'arm.txt'
    W_S = 60500. #[N]
    ap = Main(T_p,W_S,filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8)
    return ap

if __name__== "__main__":
    ap = init()
    #input = raw_input('Enter input')
    ap.firstMeasurementSeries()
    ap.secondMeasurementSeries()
    '''
    if input == '1':
        ap.shortPeriod()
    if input == '2':
        ap.phugoid()
    if input == '3':
        ap.aperiodicRoll()
    if input == '4':
        ap.dutchRoll()
    if input == '5':
        ap.aperiodicSpiral()
    '''



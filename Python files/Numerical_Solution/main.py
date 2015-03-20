__author__ = 'myth'

#clear the terminal
import os
clear = lambda: os.system('cls')
clear()
#close all plots
import matplotlib.pyplot as plt
plt.close("all")


import ISA, C_L, C_D,C_D_0, C_L_alpha,C_m_alpha,eqde,eqfe,FevsVplot,C_m_delta, C_D_alpha, input, weight,x_cg , oswaldfactor, Veq, C_LvsC_Dplot, C_L2vsC_Dplot, delta_evsVplot
import eigenvalues, Response_variables, dynamic_response, dynamic_response_plot, produce_datapoints, TAS

from Cit_par import*
from state_space import*
from numpy import*
from math import *

class Main:
    def __init__(self,W_S,filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8):                 #Initializes all the varibles needed
        print 'initializing............'
        self.W_S=W_S
        self.data,self.weights,self.statCG,self.statCLCD,self.statDEV,self.thrust,self.moment,self.arm=input.inputFile(filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8)
        #names for arrays of files: statCLCD, statDEV (for elevator-trim) and statCG (for cg_shift)

    def firstMeasurementSeries(self):   # Call all functions needed for calculation in the first measurement series
        print 'First Measurement Series Calculation: Begin'     
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
        file.write(str(self.data[29949][14]))
        file.write('\n')
        file.write(str((W[30191])/g))
        file.close()


        sys1 = stateSpaceSymmetric()
        eig_symmetric = array(eigenvalues.eigenvalues(sys1))
        eig_symmetric = eig_symmetric[0]
        result = Response_variables.Response_symmetric(eig_symmetric)
        print 'M = ',m
        print 'h = ',hp0
        print 'V = ',V0
        print 'rho = ',rho
        print 'eig = ',result[0]
        print 'P = ',result[1]
        print r'T$_{1/2}$ = ',result[2]
        print r'$\zeta$ = ',result[3]
        print r'w$_0$ = ',result[4]


        #Response values and plots

        sys2 = stateSpaceSymmetric()
        T,U1,U2,U3,U4,I = produce_datapoints.points1(self.data[2:])
        [t,y,x] = dynamic_response.dynamic_response(sys2,T,I)
        y1,y2,y3,y4 = produce_datapoints.points2(y)
        dynamic_response_plot.plot_shortPeriod(t,y1,U1,y2,U2,y3,U3,y4,U4)


        print 'Short Period Calculation: End'

    def phugoid(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Phugoid Calculation: Begin'
        W = weight.weight(self.W_S,self.weights,self.data[2:],g)
        open('input.txt', 'w').close()
        file = open('input.txt','w')
        file.write(str(self.data[30629][17]))
        file.write('\n')
        file.write(str(self.data[30629][19]))
        file.write('\n')
        file.write(str(self.data[30629][0]))
        file.write('\n')
        file.write(str(self.data[30629][12]))
        file.write('\n')
        file.write(str(self.data[30629][14]))
        file.write('\n')
        file.write(str(W[31633]/g))
        file.close()

        sys1 = stateSpaceSymmetric()
        eig_symmetric = array(eigenvalues.eigenvalues(sys1))
        eig_symmetric = eig_symmetric[2]
        result = Response_variables.Response_symmetric(eig_symmetric)
        print 'M = ',m
        print 'h = ',hp0
        print 'V = ',V0
        print 'rho = ',rho
        print 'eig = ',result[0]
        print 'P = ',result[1]
        print r'T$_{1/2}$ = ',result[2]
        print r'$\zeta$ = ',result[3]
        print r'w$_0$ = ',result[4]

        #Response values and plots

        sys2 = stateSpaceSymmetric()
        T,U1,U2,U3,U4,I = produce_datapoints.points1(self.data[2:])
        [t,y,x] = dynamic_response.dynamic_response(sys2,T,I)
        y1,y2,y3,y4 = produce_datapoints.points2(y)
        dynamic_response_plot.plot_shortPeriod(t,y1,U1,y2,U2,y3,U3,y4,U4)

        print 'Phugoid Calculation: End'


    def aperiodicRoll(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Aperiodic Roll Calculation: Begin'
        W = weight.weight(self.W_S,self.weights,self.data[2:],g)
        open('input.txt', 'w').close()
        file = open('input.txt','w')
        file.write(str(self.data[29099][17]))
        file.write('\n')
        file.write(str(self.data[29099][19]))
        file.write('\n')
        file.write(str(self.data[29099][0]))
        file.write('\n')
        file.write(str(self.data[29099][12]))
        file.write('\n')
        file.write(str(W[29309]/g))
        file.close()

        sys1 = stateSpaceAsymmetric(1)
        eig_asymmetric = array(eigenvalues.eigenvalues(sys1))
        eig_asymmetric = eig_asymmetric[0]
        result = Response_variables.Response_Asymmetric(eig_asymmetric)
        print 'M = ',m
        print 'h = ',hp0
        print 'V = ',V0
        print 'rho = ',rho
        print 'eig = ',result[0]
        print 'P = ',result[1]
        print r'T$_{1/2}$ = ',result[2]
        print r'$\zeta$ = ',result[3]
        print r'w$_0$ = ',result[4]
        print 'Phugoid Calculation: End'
        print 'Aperiodic Roll Calculation: End'

    def dutchRoll(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Dutch Roll Calculation: Begin'
        W = weight.weight(self.W_S,self.weights,self.data[2:],g)
        open('input.txt', 'w').close()
        file = open('input.txt','w')
        file.write(str(self.data[32999][17]))
        file.write('\n')
        file.write(str(self.data[32999][19]))
        file.write('\n')
        file.write(str(self.data[32999][0]))
        file.write('\n')
        file.write(str(self.data[32999][12]))
        file.write('\n')
        file.write(str(W[33310]/g))
        file.close()

        sys1 = stateSpaceAsymmetric(1)
        eig_asymmetric = array(eigenvalues.eigenvalues(sys1))
        eig_asymmetric = eig_asymmetric[1]
        result = Response_variables.Response_Asymmetric(eig_asymmetric)
        print 'M = ',m
        print 'h = ',hp0
        print 'V = ',V0
        print 'rho = ',rho
        print 'eig = ',result[0]
        print 'P = ',result[1]
        print r'T$_{1/2}$ = ',result[2]
        print r'$\zeta$ = ',result[3]
        print r'w$_0$ = ',result[4]
        print 'Phugoid Calculation: End'
        print 'Dutch Roll Calculation: End'

    def aperiodicSpiral(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Aperiodic Spiral Calculation: Begin'
        W = weight.weight(self.W_S,self.weights,self.data[2:],g)
        open('input.txt', 'w').close()
        file = open('input.txt','w')
        file.write(str(self.data[35579][17]))
        file.write('\n')
        file.write(str(self.data[35579][19]))
        file.write('\n')
        file.write(str(self.data[35579][0]))
        file.write('\n')
        file.write(str(self.data[35579][12]))
        file.write('\n')
        file.write(str(W[37097]/g))
        file.close()

        sys1 = stateSpaceAsymmetric(1)
        eig_asymmetric = array(eigenvalues.eigenvalues(sys1))
        eig_asymmetric = eig_asymmetric[3]
        result = Response_variables.Response_Asymmetric(eig_asymmetric)
        print 'M = ',m
        print 'h = ',hp0
        print 'V = ',V0
        print 'rho = ',rho
        print 'eig = ',result[0]
        print 'P = ',result[1]
        print r'T$_{1/2}$ = ',result[2]
        print r'$\zeta$ = ',result[3]
        print r'w$_0$ = ',result[4]
        print 'Phugoid Calculation: End'
        print 'Aperiodic Spiral Calculation: End'


def init():
    """

    :rtype : object
    """
    filename1 = 'FTISxprt-20150305_144557.txt'
    filename2 = 'weights.txt'
    filename3 = 'stationary_cg_shift.txt'
    filename4 = 'stationary_CL-CD.txt'
    filename5 = 'stationary_elevator-trim.txt'
    filename6 = 'statthrust.dat'
    filename7 = 'fuel_moments.txt'
    filename8 = 'arm.txt'
    W_S = 9170/0.224808943 #[N]
    ap = Main(W_S,filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8)
    return ap

if __name__== "__main__":
    ap = init()
    input = raw_input('Enter input')
    #ap.firstMeasurementSeries()
    #ap.secondMeasurementSeries()

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




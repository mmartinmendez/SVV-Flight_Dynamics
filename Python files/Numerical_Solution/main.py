__author__ = 'myth'

from Numerical_Solution import *

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


    def firstMeasurementSeries(self):               # Call all functions needed for calculation in the first measurement series
        print 'First Measurement Series Calculation: Begin'
        a,b,c = ISA.aparameters(self.h1)
     #   W = weight.weight(self.W_S,self.weights,self.data[6:8])
        lst = array(self.data[6])
        print lst

        print 'First Measurement Series Calculation: End'

    def secondMeasurementSeries(self):              # Call all functions needed for calculation in the second measurement series
        print 'Second Measurement Series Calculation: Begin'
        print 'Second Measurement Series Calculation: End'

    def dynamicMeasurementSeries(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Dynamic Measurement Series Calculation: Begin'
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


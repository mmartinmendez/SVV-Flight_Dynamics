__author__ = 'myth'

from Numerical_Solution import *

class Main:
    def __init__(self,h,p,S,V,T_p,W_S):                 #Initializes all the varibles needed
        print 'initializing............'
        self.h1=h
        self.p=p
        self.S=S
        self.V=V
        self.T_p=T_p
        self.W_S=W_S

    def firstMeasurementSeries(self):               # Call all functions needed for calculation in the first measurement series
        print 'First Measurement Series Calculation: Begin'
        a,b,c = IAS.aparameters(self.h1)
        W = weight(self.W_S)
        print 'First Measurement Series Calculation: End'

    def secondMeasurementSeries(self):              # Call all functions needed for calculation in the second measurement series
        print 'Second Measurement Series Calculation: Begin'
        print 'Second Measurement Series Calculation: End'

    def dynamicMeasurementSeries(self):             # Call all functions needed for calculation in the dynamic measurement series
        print 'Dynamic Measurement Series Calculation: Begin'
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
    W_S = 60500 #[N]
    ap = Main(h,p,S,V,T_p,W_S)
    return ap

if __name__== "__main__":
    ap = init()
    ap.firstMeasurementSeries()
    ap.secondMeasurementSeries()
    ap.dynamicMeasurementSeries()


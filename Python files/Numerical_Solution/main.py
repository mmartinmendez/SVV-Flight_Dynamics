__author__ = 'myth'

from Numerical_Solution import*

class Main:
    def __init__(self,h,p,S,V,T_p,filename):                 #Initializes all the varibles needed
        print 'initializing............'
        self.h1=h
        self.p=p
        self.S=S
        self.V=V
        self.T_p=T_p
        self.filename=filename

    def importFile(self):
        data = input.inputFile(self.filename)

    def firstMeasurementSeries(self):               # Call all functions needed for calculation in the first measurement series
        print 'First Measurement Series Calculation: Begin'
        a,b,c = ISA.aparameters(self.h1)
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
    filename = 'fags.txt'
    ap = Main(h,p,S,V,T_p,filename)
    return ap

if __name__== "__main__":
    ap = init()
    ap.importFile()
    ap.firstMeasurementSeries()
    ap.secondMeasurementSeries()
    ap.dynamicMeasurementSeries()


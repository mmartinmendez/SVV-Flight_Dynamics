__author__ = 'myth'


import IAS
import C_D


class Main:
    def __init__(self,h,p,S,V,T_p):
        print 'initializing'
        self.h1=h
        self.p=p
        self.S=S
        self.V=V
        self.T_p=T_p

    def atmospheric_paramter(self):
        a,b,c = IAS.aparameters(self.h1)
        print a
        print b
        print c
        d=C_D.C_D(c,self.S,self.V,self.T_p)
        print d


def init():
    """

    :rtype : object
    """
    h=0
    p=12000.
    S=15
    V=100
    T_p=1200
    ap = Main(h,p,S,V,T_p)
    return ap

if __name__== "__main__":
    ap = init()
    ap.atmospheric_paramter()


__author__ = 'myth'


import IAS


class Main:
    def __init__(self):
        print 'initializing'

    def atmospheric_paramter(self):
        a,b,c = IAS.aparameters(1000.)
        print a
        print b
        print c

def init():
    ap = Main()
    return ap

if __name__== "__main__":
    ap = init()
    ap.atmospheric_paramter()
